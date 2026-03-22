import streamlit as st
import time

# --- 1. GLOBAL BRANDING ---
st.set_page_config(page_title="Sisi Sacco", page_icon="S", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .splash-container {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.95)), 
                    url('https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1500&q=80');
        background-size: cover; z-index: 9999; display: flex; flex-direction: column; 
        align-items: center; justify-content: center; color: white; text-align: center;
    }
    .s-red { color: #ef4444; } .s-green { color: #10b981; }
    .loader-bar { width: 300px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; margin-top: 20px;}
    .loader-progress { width: 0%; height: 100%; background: #10b981; animation: load 4s linear forwards; }
    @keyframes load { 0% { width: 0%; } 100% { width: 100%; } }
    .vault-card { background: white; border-radius: 20px; padding: 25px; border-left: 8px solid #10b981; box-shadow: 0 10px 20px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 50px; height: 3rem; background: #10b981; color: white !important; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE SOVEREIGN STATE ROUTER ---
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'splash'
if 'hierarchy' not in st.session_state:
    st.session_state.hierarchy = {'overseer': None, 'chair': None, 'treasurer': None, 'secretary': None}

# --- 3. PHASE 0: THE CINEMATIC SPLASH ---
if st.session_state.app_state == 'splash':
    p = st.empty()
    with p.container():
        st.markdown('<div class="splash-container"><h1><span class="s-red">S</span>ISI <span class="s-green">SACCO</span></h1><p>THE INVITER: STRENGTH IN UNITY</p></div>', unsafe_allow_html=True)
        time.sleep(5)
    with p.container():
        st.markdown('<div class="splash-container"><h3>ESTABLISHING TRUST HIERARCHY...</h3><div class="loader-bar"><div class="loader-progress"></div></div></div>', unsafe_allow_html=True)
        time.sleep(4)
    st.session_state.app_state = 'election_overseer'
    st.rerun()

# --- 4. PHASE 1: ELECTION OF THE OVERSEER (Foundation) ---
if st.session_state.app_state == 'election_overseer':
    st.title("⚖️ Election Phase 1: The Overseer")
    st.info("The Overseer is the foundation. They watch the Leaders and the Treasury.")
    name = st.text_input("Enter Nominee for Overseer:")
    if st.button("Confirm Overseer Election"):
        st.session_state.hierarchy['overseer'] = name
        st.session_state.app_state = 'election_leaders'
        st.rerun()

# --- 5. PHASE 2: NOMINATION OF LEADERS (Rising Upward) ---
elif st.session_state.app_state == 'election_leaders':
    st.title("⬆️ Election Phase 2: Rising Hierarchy")
    st.write(f"**Overseer:** {st.session_state.hierarchy['overseer']} (Watching)")
    col1, col2, col3 = st.columns(3)
    with col1:
        chair = st.text_input("Nominate Chair:")
    with col2:
        treasurer = st.text_input("Nominate Treasurer:")
    with col3:
        secretary = st.text_input("Nominate Secretary:")
    
    if st.button("Finalize Executive Board"):
        st.session_state.hierarchy.update({'chair': chair, 'treasurer': treasurer, 'secretary': secretary})
        st.session_state.app_state = 'chair_selection'
        st.rerun()

# --- 6. PHASE 3: CHAIR CHOOSES THE PLAN (Overseen by Overseer) ---
elif st.session_state.app_state == 'chair_selection':
    st.title(f"👑 Chair's Decision: {st.session_state.hierarchy['chair']}")
    st.warning(f"Overseer {st.session_state.hierarchy['overseer']} is monitoring this selection.")
    
    plan_type = st.radio("Select Primary Strategy:", ["6-Month Growth", "12-Month Sovereign Yearly"])
    sub_plan = st.selectbox("Select Sub-Plan Level:", ["Bronze (Hustler)", "Silver (Standard)", "Gold (Elite)"])
    
    if st.button("Confirm Strategy"):
        st.session_state.selected_plan = {"main": plan_type, "sub": sub_plan}
        st.session_state.app_state = 'treasurer_payment'
        st.rerun()

# --- 7. PHASE 4: TREASURER PAYS (Overseen by Chair & Overseer) ---
elif st.session_state.app_state == 'treasurer_payment':
    st.title(f"💰 Treasurer's Execution: {st.session_state.hierarchy['treasurer']}")
    st.write(f"Executing Payment for: **{st.session_state.selected_plan['main']} - {st.session_state.selected_plan['sub']}**")
    
    st.markdown(f"""
    <div style='background: #fee2e2; padding: 20px; border-radius: 15px; border: 1px solid #ef4444;'>
        <b>Verification Protocol Active:</b><br>
        1. Chair ({st.session_state.hierarchy['chair']}): APPROVED<br>
        2. Overseer ({st.session_state.hierarchy['overseer']}): WATCHING
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Trigger M-Pesa Ratiba B2B Payment"):
        with st.spinner("Processing Treasury Handshake..."):
            time.sleep(3)
            st.session_state.app_state = 'final_dashboard'
            st.rerun()

# --- 8. PHASE 5: THE FINAL DASHBOARD ---
elif st.session_state.app_state == 'final_dashboard':
    st.balloons()
    st.title("🏛️ Sisi Sacco Sovereign Vault")
    
    # Hierarchy Display
    with st.expander("View Active Governance Hierarchy"):
        st.write(f"**Overseer:** {st.session_state.hierarchy['overseer']}")
        st.write(f"**Chair:** {st.session_state.hierarchy['chair']}")
        st.write(f"**Treasurer:** {st.session_state.hierarchy['treasurer']}")
    
    st.divider()
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Vault Status", st.session_state.selected_plan['main'])
    m2.metric("Tier", st.session_state.selected_plan['sub'])
    m3.metric("System Integrity", "100%", "y + 4 Verified")

    t1, t2 = st.tabs(["Wallet", "Governance"])
    with t1:
        st.markdown("<div class='vault-card'><h3>Portfolio</h3><p>Payments verified by Treasurer.</p></div>", unsafe_allow_html=True)
    with t2:
        st.info("The 2/3 Member Vote can reset this hierarchy at any time.")
