import streamlit as st
import pandas as pd
import time

# --- APP CONFIGURATION ---
st.set_page_config(page_title="As We Rise | Chama Sacco", page_icon="🤝", layout="wide")

# --- INITIALIZE DUMMY DATA (Session State) ---
if 'member_savings' not in st.session_state:
    st.session_state.member_savings = 15000.0  # The 95% Bucket
    st.session_state.emergency_fund = 750.0    # The 5% Bucket
    st.session_state.chama_vault = 50000.0     # Group Stability Capital
    st.session_state.is_subscribed = False
    st.session_state.fines = 0
    st.session_state.tasks = ["Verify Land Rates", "Update Minutes", "Check M-Pesa Logs"]

# --- CUSTOM CSS FOR ATTRACTIVE UI ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .slogan { font-style: italic; color: #555; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER & SLOGAN ---
st.title("🤝 As We Rise | Modern Chama Sacco")
st.markdown("<p class='slogan'>\"Empowering our future, one contribution at a time.\"</p>", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://img.icons8.com/ios-filled/100/2ecc71/handshake.png", width=100)
st.sidebar.title("Main Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Personal Dashboard", 
    "📈 Group Vault & Investments", 
    "🗳️ Governance & Elections", 
    "🚨 Emergency Protocol",
    "📋 Objective To-Do List",
    "⚙️ Admin & Subscription"
])

# --- 1. PERSONAL DASHBOARD ---
if page == "🏠 Personal Dashboard":
    st.header("👤 My Member Profile")
    
    # Realistic Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Personal Savings (95%)", f"KES {st.session_state.member_savings:,.2f}")
    
    # Calculate emergency fund with 3.5% interest
    emer_with_interest = st.session_state.emergency_fund * 1.035
    col2.metric("Emergency Fund (5%)", f"KES {emer_with_interest:,.2f}", "+3.5% Interest")
    
    col3.metric("Outstanding Fines", f"KES {st.session_state.fines}", delta_color="inverse")

    st.markdown("---")
    
    # M-PESA DEPOSIT SIMULATION
    st.subheader("📲 M-Pesa Deposit (Safaricom Integrated)")
    amount = st.number_input("Enter Amount to Deposit:", min_value=100, step=100)
    freq = st.selectbox("Cycle Frequency:", ["Daily", "Weekly", "Monthly"])
    
    if st.button("Deposit via STK Push"):
        with st.spinner("Requesting M-Pesa PIN..."):
            time.sleep(2) # Simulating API latency
            
            # THE MATH ENGINE
            tax = amount * 0.05
            net_savings = amount * 0.95
            
            st.session_state.member_savings += net_savings
            st.session_state.emergency_fund += tax
            st.session_state.chama_vault += (tax * 0.1) # Small portion to Chama stability
            
            st.success(f"Successfully deposited KES {amount}. {freq} contribution updated!")
            st.balloons()

# --- 2. GROUP VAULT & INVESTMENTS ---
elif page == "📈 Group Vault & Investments":
    st.header("🏦 Group Financial Hub")
    
    st.metric("Total Chama Stability Capital", f"KES {st.session_state.chama_vault:,.2f}")
    
    tab1, tab2, tab3 = st.tabs(["🔄 Merry-Go-Round", "💸 Table Banking", "🏗️ Wealth Creation"])
    
    with tab1:
        st.write("Current Rotation Cycle: **Round 4 of 20**")
        st.write("Next Beneficiary: **John Doe (Member #5)**")
        st.progress(0.2, text="Total Group Goal Progress")
        
    with tab2:
        st.subheader("Request a Loan")
        max_loan = st.session_state.member_savings * 3
        st.write(f"Your Loan Limit (3x Savings): **KES {max_loan:,.2f}**")
        loan_req = st.number_input("Loan Amount Requested:", max_value=int(max_loan))
        if st.button("Request Loan (Requires 2/3 Vote)"):
            st.info("Request sent to the Governance board for member voting.")
            
    with tab3:
        st.write("The 5% retained funds are currently invested in:")
        st.markdown("- **Nanyuki Plot #402** (Real Estate)")
        st.markdown("- **Safaricom Stocks** (NSE Portfolio)")
        st.markdown("- **Poultry Farming Project** (Active)")

# --- 3. GOVERNANCE & ELECTIONS ---
elif page == "🗳️ Governance & Elections":
    st.header("🗳️ Democratic Portal")
    st.write("All decisions require a **2/3 Majority**.")
    
    st.subheader("Secret Ballot: Chair Election")
    st.radio("Select Candidate:", ["Candidate A", "Candidate B", "Candidate C"])
    if st.button("Cast Secret Vote"):
        st.success("Your vote has been securely encrypted and cast.")

# --- 4. EMERGENCY PROTOCOL ---
elif page == "🚨 Emergency Protocol":
    st.header("🛡️ Triple-Lock Safety System")
    st.warning("This protocol triggers funds for Death or Medical Emergencies.")
    
    st.markdown("""
    **Required Step 1:** Chair Notifies 🔔  
    **Required Step 2:** Overseer Confirms ✅  
    **Required Step 3:** Member Seconds 👤
    """)
    
    if st.button("CHAIR: Initiate Emergency Notification"):
        st.error("Emergency Alert Sent! Awaiting Overseer and Member verification.")

# --- 5. OBJECTIVE TO-DO LIST ---
elif page == "📋 Objective To-Do List":
    st.header("📝 Chama Objectives")
    new_task = st.text_input("Secretary: Add new task to list")
    if st.button("Add Task"):
        st.session_state.tasks.append(new_task)
    
    for task in st.session_state.tasks:
        st.checkbox(task)

# --- 6. ADMIN & SUBSCRIPTION ---
elif page == "⚙️ Admin & Subscription":
    st.header("👑 Leadership Dashboard")
    st.info("The Overseer can manage members here (Cap: 20).")
    
    st.selectbox("Subscription Plan:", ["6 Months (KES 6,000)", "1 Year (KES 13,000)"])
    if st.button("Pay Subscription (Dummy)"):
        st.session_state.is_subscribed = True
        st.success("App Unlocked for all members!")
