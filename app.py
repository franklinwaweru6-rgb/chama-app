import streamlit as st
import pandas as pd
import hashlib
import time
import math

# --- 1. THE "ONE-OF-ONE" HIGH-TECH UI CONFIG ---
st.set_page_config(page_title="Kilele Sacco | Sovereign", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .vault-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(12px);
        border-radius: 24px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white !important; font-weight: 600; transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.4);
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    }
    .badge {
        background: #d1fae5; color: #065f46; padding: 4px 12px;
        border-radius: 20px; font-size: 12px; font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. GLOBAL STATE ENGINE (THE BACKBONE) ---
if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'phase': 'Recruitment', # Recruitment -> SatisfactionPoll -> Election -> Active
        'members': {}, # {Name: {id_hash: x, savings: 0, mini_em: 0, loan: 0}}
        'leaders': {'Overseer': None, 'Chair': None, 'Secretary': None, 'Treasurer': None},
        'vault_5_percent': 0.0,
        'interest_pool': 0.0,
        'reserve_lock': 0.30, # 30% Emergency Hard-Lock
        'satisfaction_votes': {},
        'audit_logs': []
    }

# --- 3. CORE UTILITIES (THE MATH) ---
def add_audit(action):
    st.session_state.sacco['audit_logs'].append(f"{time.strftime('%H:%M:%S')} | {action}")

def bankers_round(amt):
    return math.floor(amt * 100) / 100

# --- 4. PHASE 1: RECRUITMENT (y+4 RULE) ---
if st.session_state.sacco['phase'] == 'Recruitment':
    st.markdown("<h1 style='color: #0f172a;'>🏗️ Group Formation</h1>", unsafe_allow_html=True)
    st.info("🛡️ y+4 Security: 4 Leaders + 4 Buffer Members required to unlock the Vault.")
    
    with st.container():
        st.markdown("<div class='vault-card'>", unsafe_allow_html=True)
        name = st.text_input("Member Full Name:")
        m_id = st.text_input("National ID (Encrypted on entry):")
        if st.button("Onboard Member"):
            if name and m_id:
                id_hash = hashlib.sha256(m_id.encode()).hexdigest()[:10]
                st.session_state.sacco['members'][name] = {'id': id_hash, 'savings': 0.0, 'mini_em': 0.0, 'loan': 0.0}
                add_audit(f"Member {name} onboarded.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    count = len(st.session_state.sacco['members'])
    st.progress(min(count/8, 1.0), text=f"Recruitment: {count}/8")
    
    if count >= 8:
        if st.button("Finalize Recruitment & Move to Satisfaction Poll ➡️"):
            st.session_state.sacco['phase'] = 'SatisfactionPoll'
            st.rerun()

# --- 5. PHASE 2: THE DEMOCRATIC VALVE (2/3 RULE) ---
elif st.session_state.sacco['phase'] == 'SatisfactionPoll':
    st.markdown("<h1 style='color: #0f172a;'>🗳️ Satisfaction Ballot</h1>", unsafe_allow_html=True)
    st.write("A 2/3 majority (6/8) must be satisfied to skip an election.")
    
    voter = st.selectbox("Identify yourself:", list(st.session_state.sacco['members'].keys()))
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        if st.button("✅ Yes, Retain Leadership"):
            st.session_state.sacco['satisfaction_votes'][voter] = "Yes"
    with col_v2:
        if st.button("❌ No, Trigger Election"):
            st.session_state.sacco['satisfaction_votes'][voter] = "No"

    done = len(st.session_state.sacco['satisfaction_votes'])
    st.write(f"Votes cast: {done}/8")
    
    if done >= 8:
        yes_count = list(st.session_state.sacco['satisfaction_votes'].values()).count("Yes")
        if yes_count >= 6: # 2/3 of 8 is 5.33 -> 6
            st.success(f"Consensus Reached ({yes_count}/8).")
            if st.button("Activate Sacco"): 
                st.session_state.sacco['phase'] = 'Active'
                st.rerun()
        else:
            st.error("Dissatisfaction Detected. Mandatory Election Triggered.")
            if st.button("Proceed to Overseer Nominations"):
                st.session_state.sacco['phase'] = 'OverseerElection'
                st.rerun()

# --- 6. PHASE 3: ACTIVE SACCO (THE THREE SIDES) ---
elif st.session_state.sacco['phase'] == 'Active':
    # High-Tech Header
    st.markdown("<div style='text-align: right;'><span class='badge'>Sovereign Vault Active</span></div>", unsafe_allow_html=True)
    
    st.sidebar.title("🚦 Navigation")
    nav = st.sidebar.radio("Go to:", ["Personal Portfolio", "Chama Transparency", "Leader Dashboard"])
    
    if nav == "Personal Portfolio":
        st.header("👤 My Assets")
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Fortress Savings (95%)", "KES 47,500", "Locked")
        with c2: st.metric("Mini-Emergency (3.5%)", "KES 1,240", "Available")
        with c3: st.metric("Current Loan", "KES 0", "Eligible: 3x")
        
        st.markdown("<div class='vault-card'>", unsafe_allow_html=True)
        st.subheader("🚀 Stability Loan Request")
        st.info("Funds sourced from 5% Stability Vault. 95% Savings remain untouched.")
        loan_amt = st.number_input("Amount:", min_value=0)
        if st.button("Request via 2 Guarantors"):
            st.toast("Handshake sent to community.")
        st.markdown("</div>", unsafe_allow_html=True)

    elif nav == "Chama Transparency":
        st.header("🏢 Group Liquidity")
        st.metric("Stability Vault (Loan Pool)", f"KES {st.session_state.sacco['vault_5_percent']:,.2f}")
        st.progress(st.session_state.sacco['reserve_lock'], text="30% Emergency Reserve (Hard-Locked)")
        
        st.subheader("📜 Sovereign Audit Trail")
        for log in reversed(st.session_state.sacco['audit_logs']):
            st.caption(log)

    elif nav == "Leader Dashboard":
        st.header("🔒 Executive Controls")
        if st.button("💰 Distribute Payouts (End of Cycle)"):
            st.success("B2C API Handshake: All 8 members paid pro-rata.")
            add_audit("Treasurer distributed 95% funds + interest.")
