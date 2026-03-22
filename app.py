import streamlit as st
import pandas as pd

# --- 1. PREMIUM CUSTOM STYLING (THE DESIGN) ---
st.set_page_config(page_title="As We Rise | Sacco Pro", page_icon="🤝", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f1f5f9; }
    div[data-testid="stMetricValue"] { color: #059669; font-weight: 800; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #059669; color: white; border: none; font-weight: bold; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
    .stButton>button:hover { background-color: #047857; transform: translateY(-1px); }
    .card { background-color: white; padding: 2rem; border-radius: 1rem; border-left: 6px solid #10b981; box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1); margin-bottom: 1rem; }
    .slogan { font-style: italic; color: #065f46; text-align: center; font-size: 1.2rem; margin-bottom: 2rem; }
    .status-badge { padding: 4px 12px; border-radius: 15px; font-size: 0.8rem; background-color: #d1fae5; color: #065f46; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL SYSTEM CONTROLLER (THE M-PESA SIDE BACKEND) ---
if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'phase': 'Picker', # Picker -> Subscription -> OverseerInterest -> OverseerBallot -> MainElection -> Active
        'members': {},      # {Name: {'id': ID, 'balance': 0, 'mini_em': 0}}
        'leaders': {'Overseer': None, 'Chair': None, 'Secretary': None, 'Treasurer': None},
        'candidates': [],   # Dynamic list for elections
        'cycle_type': None, # 6-Month or Yearly
        'vault_total': 0.0,
        'funds_distributed': False,
        'interest_rate': 3.5,
        'votes': {}
    }

st.markdown("<h1 style='text-align: center; color: #0f172a;'>🤝 As We Rise</h1>", unsafe_allow_html=True)
st.markdown("<p class='slogan'>Empowering our future, one contribution at a time.</p>", unsafe_allow_html=True)

# --- 3. PHASE 1: THE PICKER (INVITER) & y+4 RULE ---
if st.session_state.sacco['phase'] == 'Picker':
    st.header("🏗️ Step 1: Member Recruitment")
    st.info("🛡️ Security Rule: Minimum 8 Members (4 Leaders + 4 Buffer) required to balance power.")
    
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        m_name = st.text_input("Member Full Name (M-Pesa Verified):")
        m_id = st.text_input("National ID Number:")
        if st.button("Add Member to Sacco Ledger"):
            if m_name and m_id:
                st.session_state.sacco['members'][m_name] = {'id': m_id, 'balance': 1000.0, 'mini_em': 500.0}
                st.success(f"Verified: {m_name} added.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    count = len(st.session_state.sacco['members'])
    st.progress(min(count / 8, 1.0), text=f"Recruitment Progress: {count}/8")

    if count >= 8:
        if st.button("Finish Recruitment & View Plans ➡️"):
            st.session_state.sacco['phase'] = 'Subscription'
            st.rerun()

# --- 4. PHASE 2: DYNAMIC SUBSCRIPTION GATE ---
elif st.session_state.sacco['phase'] == 'Subscription':
    count = len(st.session_state.sacco['members'])
    st.header("💳 Treasurer: Activation & Cycle Selection")
    
    # Pricing Tier Logic
    if count <= 10: fee = 2000
    elif count <= 20: fee = 2500
    else: fee = 3500

    st.write(f"Group Tier: **{count} Members** | Monthly Service Fee: **KES {fee}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='card'><h3>🗓️ 6-Month Cycle</h3><p>KES {fee}/mo</p></div>", unsafe_allow_html=True)
        if st.button("Activate 6-Month Plan"):
            st.session_state.sacco['cycle_type'] = "6-Month"
            st.session_state.sacco['phase'] = 'OverseerInterest'
            st.rerun()
    with col2:
        st.markdown(f"<div class='card'><h3>📅 Yearly Cycle</h3><p>KES {fee}/mo</p></div>", unsafe_allow_html=True)
        if st.button("Activate Yearly Plan"):
            st.session_state.sacco['cycle_type'] = "Yearly"
            st.session_state.sacco['phase'] = 'OverseerInterest'
            st.rerun()

# --- 5. PHASE 3: CASCADING ELECTIONS (OVERSEER FIRST) ---
elif st.session_state.sacco['phase'] == 'OverseerInterest':
    st.header("⚖️ Election: The Overseer")
    st.write("Candidates: Register your interest for the highest rank.")
    
    interest_name = st.selectbox("Select your name:", list(st.session_state.sacco['members'].keys()))
    if st.button("I Want to Run for Overseer"):
        if interest_name not in st.session_state.sacco['candidates']:
            st.session_state.sacco['candidates'].append(interest_name)
            st.success(f"{interest_name} is on the ballot.")

    if len(st.session_state.sacco['candidates']) >= 2:
        if st.button("Close Nominations & Start Voting"):
            st.session_state.sacco['phase'] = 'OverseerBallot'
            st.rerun()

elif st.session_state.sacco['phase'] == 'OverseerBallot':
    st.header("🗳️ Secret Ballot: Overseer")
    voter = st.selectbox("Identify yourself:", list(st.session_state.sacco['members'].keys()))
    vote_for = st.radio("Cast Vote For:", st.session_state.sacco['candidates'])
    
    if st.button("Cast Secret Vote"):
        if voter not in st.session_state.sacco['votes']:
            st.session_state.sacco['votes'][voter] = vote_for
            st.success("Vote Recorded.")
        else: st.error("Access Denied: Already Voted.")

    if st.button("Tally Overseer Results"):
        res = pd.Series(st.session_state.sacco['votes'].values()).value_counts()
        winners = res[res == res.max()].index.tolist()
        
        if len(winners) > 1:
            st.warning("⚠️ TIE DETECTED. Runoff triggered between top 2.")
            st.session_state.sacco['candidates'] = winners
            st.session_state.sacco['votes'] = {}
            st.rerun()
        else:
            st.session_state.sacco['leaders']['Overseer'] = winners[0]
            st.session_state.sacco['phase'] = 'Active' # Simplifying for this build
            st.success(f"🎊 {winners[0]} is the Overseer!")
            st.rerun()

# --- 6. PHASE 4: ACTIVE SYSTEM (THE THREE SIDES) ---
elif st.session_state.sacco['phase'] == 'Active':
    st.sidebar.title("🚦 Sacco Navigation")
    side = st.sidebar.radio("View Dashboard:", ["Member Side", "Chama Side", "M-Pesa Side (Admin)"])
    role = st.sidebar.selectbox("Access As:", ["Member", "Chair", "Secretary", "Treasurer", "Overseer"])

    if side == "Member Side":
        st.header(f"👤 {role} Portfolio")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Savings (95%)", "KES 12,400")
            st.write("**📊 Loan Gauge (3x)**")
            st.progress(0.2, text="Used: KES 5,000 / 37,200")
        with c2:
            st.metric(f"Mini-Emergency ({st.session_state.sacco['interest_rate']}%)", "KES 4,500")
            if st.button("Withdraw Small Emergency"): st.warning("Sending STK Push...")

    elif side == "Chama Side":
        st.header("🏢 Collective Chama Wall")
        st.markdown(f"**Cycle Mode:** {st.session_state.sacco['cycle_type']} <span class='status-badge'>Active</span>", unsafe_allow_html=True)
        st.metric("Total Group Vault", f"KES {st.session_state.sacco['vault_total']:,.2f}")
        
        if role == "Chair":
            if st.button("🚨 Notify Triple-Lock Emergency"):
                st.error("Emergency sequence initiated. Awaiting Overseer verification.")

    elif side == "M-Pesa Side (Admin)":
        st.header("🔒 M-Pesa Side (Treasurer Only)")
        
        if role == "Treasurer":
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("🏁 End of Cycle Operations")
            if st.button("💰 Distribute Funds (Pro-Rata 95/5)"):
                st.session_state.sacco['funds_distributed'] = True
                st.success("Payouts sent to all members based on contribution percentage.")
            
            if st.session_state.sacco['funds_distributed']:
                st.markdown("---")
                new_p = st.selectbox("Change Package?", ["Remain Current", "Upgrade Tier", "Downgrade Tier"])
                if st.button("Renew Subscription"):
                    st.session_state.sacco['funds_distributed'] = False
                    st.balloons()
            else:
                st.error("Renewal Locked: You must distribute the previous cycle's funds first.")
            st.markdown("</div>", unsafe_allow_html=True)
