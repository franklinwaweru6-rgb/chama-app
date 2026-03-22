import streamlit as st
import pandas as pd
import time

# --- 1. APP CONFIG & STYLING ---
st.set_page_config(page_title="As We Rise | Sacco Pro", page_icon="🤝", layout="wide")

# Custom Professional CSS
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #2ecc71; color: white; border: none; }
    .stButton>button:hover { background-color: #27ae60; border: none; }
    .card { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; border-left: 5px solid #2ecc71; }
    .stat-val { font-size: 24px; font-weight: bold; color: #2c3e50; }
    .slogan { font-style: italic; color: #27ae60; text-align: center; font-size: 1.2em; margin-top: -20px; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE (The Brain) ---
if 'subscribed' not in st.session_state:
    st.session_state.update({
        'subscribed': False,
        'members': ["Chair", "Secretary", "Treasurer", "Overseer"], # Start with leaders
        'member_cap': 20,
        'vault_balance': 50000.0,
        'personal_savings': 1500.0,
        'emergency_bucket': 75.0,
        'fines': 0,
        'tasks': ["Pay Land Rates", "Verify June Minutes"]
    })

# --- 3. THE SUBSCRIPTION GATE (LANDING PAGE) ---
if not st.session_state.subscribed:
    st.title("🤝 As We Rise | Modern Chama")
    st.markdown("<p class='slogan'>\"Empowering our future, one contribution at a time.\"</p>", unsafe_allow_html=True)
    
    st.markdown("### 🔐 Secure Member Portal")
    st.info("The Treasurer must select a package to activate this Chama's digital ledger.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""<div class='card'><h4>📅 Half-Year Growth</h4><p>Up to 20 Members</p><h3>KES 6,000</h3><ul><li>M-Pesa Integrated</li><li>Triple-Lock Emergency</li><li>Table Banking Hub</li></ul></div>""", unsafe_allow_html=True)
        if st.button("Subscribe: 6 Months"):
            with st.spinner("Processing Safaricom Merchant Request..."):
                time.sleep(2)
                st.session_state.subscribed = True
                st.rerun()

    with col_b:
        st.markdown("""<div class='card'><h4>🗓️ Annual Excellence</h4><p>Up to 20 Members</p><h3>KES 13,000</h3><ul><li>Everything in 6 Months</li><li>Priority NSE Support</li><li>Dividend Analytics</li></ul></div>""", unsafe_allow_html=True)
        if st.button("Subscribe: 12 Months"):
            st.session_state.subscribed = True
            st.rerun()
    st.stop()

# --- 4. THE MAIN SACCO DASHBOARD (Unlocked) ---
st.sidebar.markdown("# 🤝 As We Rise")
st.sidebar.markdown("---")
role = st.sidebar.selectbox("Access Level:", ["Member", "Secretary", "Treasurer", "Overseer", "Chair"])
menu = st.sidebar.radio("Navigation:", ["Dashboard", "Vault & Loans", "Governance", "Welfare", "Admin"])

# --- DASHBOARD ---
if menu == "Dashboard":
    st.header(f"Welcome back, {role}")
    
    # 3-Way Financial View
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='card'>👤 Personal Savings (95%)<br><span class='stat-val'>KES {st.session_state.personal_savings:,.2f}</span></div>", unsafe_allow_html=True)
    with c2:
        emer_val = st.session_state.emergency_bucket * 1.035
        st.markdown(f"<div class='card'>🛡️ Emergency Fund (5%)<br><span class='stat-val'>KES {emer_val:,.2f}</span><br><small>Growing at 3.5% Interest</small></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='card'>🏦 Group Stability Vault<br><span class='stat-val'>KES {st.session_state.vault_balance:,.2f}</span></div>", unsafe_allow_html=True)

    st.markdown("### 📲 Quick Deposit")
    amt = st.number_input("Amount (KES):", min_value=100)
    if st.button("Send M-Pesa STK Push"):
        st.success(f"STK Push sent to Member phone! (95% to Savings, 5% to Emergency)")

# --- VAULT & LOANS ---
elif menu == "Vault & Loans":
    st.header("📈 Financial Hub")
    t1, t2 = st.tabs(["💸 Table Banking", "🔄 Merry-Go-Round"])
    
    with t1:
        limit = st.session_state.personal_savings * 3
        st.markdown(f"<div class='card'><h4>Your Loan Limit: KES {limit:,.2f}</h4><p>Based on 3x your current savings.</p></div>", unsafe_allow_html=True)
        loan_amt = st.number_input("Request Amount:", max_value=int(limit))
        if st.button("Apply for Loan"):
            st.warning("Request submitted. Awaiting 2/3 Member Approval.")
            
    with t2:
        st.write("Current Pot Winner: **Member #5**")
        st.progress(0.4, text="Cycle Progress")

# --- GOVERNANCE ---
elif menu == "Governance":
    st.header("🗳️ Decision Room")
    st.markdown("<div class='card'><h4>Active Election: New Treasurer</h4><p>30-Day Transition Clock: 24 Days Remaining</p></div>", unsafe_allow_html=True)
    st.radio("Your Secret Ballot:", ["John Kamau", "Mary Atieno", "Bypass Candidate"])
    if st.button("Submit Anonymous Vote"):
        st.success("Vote recorded. Results hidden until quorum reached.")

# --- WELFARE (Emergency) ---
elif menu == "Welfare":
    st.header("🚨 Triple-Lock Emergency Chain")
    st.markdown("""<div class='card'>1. Chair Notifies ➡️ 2. Overseer Confirms ➡️ 3. Member Seconds</div>""", unsafe_allow_html=True)
    
    if role == "Chair":
        if st.button("🔔 Notify Group of Emergency"):
            st.error("Notification broadcasted to all members.")
    
    st.markdown("---")
    st.subheader("📋 Next of Kin (NOK) - Locked")
    st.write("Details only visible to Chair/Overseer upon full verification.")

# --- ADMIN (Overseer/Secretary Tools) ---
elif menu == "Admin":
    if role == "Overseer":
        st.header("👤 Member Management")
        count = len(st.session_state.members)
        st.write(f"Members: {count} / {st.session_state.member_cap}")
        if count < st.session_state.member_cap:
            new_mem = st.text_input("New Member Full Name:")
            if st.button("Add to Sacco"):
                st.session_state.members.append(new_mem)
                st.success(f"{new_mem} added!")
        else:
            st.error("Membership Cap Reached! (20/20)")

    if role == "Secretary":
        st.header("📝 Objective List")
        for task in st.session_state.tasks:
            st.checkbox(task, key=task)
