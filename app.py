import streamlit as st
import time

# --- 1. PREMIUM STYLING ---
st.set_page_config(page_title="As We Rise | Modern Sacco", page_icon="🤝", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f4f8; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 4px solid #27ae60; }
    .card-box { background-color: #ffffff; padding: 25px; border-radius: 15px; border-left: 8px solid #27ae60; margin-bottom: 20px; }
    .slogan { font-style: italic; color: #27ae60; text-align: center; font-size: 1.3em; margin-bottom: 30px; }
    .status-badge { padding: 5px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold; background-color: #e8f5e9; color: #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE M-PESA CONTROLLER (Backend State) ---
# This is the "Invisible Side" only you and Safaricom control
if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'active': False,
        'phase': 'Picker', # Picker -> Election -> Live
        'members': [],
        'package_limit': 20, # Default for KES 2,500/mo tier
        'leader_roles': {'Chair': None, 'Secretary': None, 'Treasurer': None, 'Overseer': None},
        'emergency_trigger': None, # Chair -> Overseer -> Member sequence
        'chama_vault': 250000.0,
        'personal_savings': 12000.0,
        'mini_emergency': 4500.0,
        'fines': 0
    }

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🤝 As We Rise</h1>", unsafe_allow_html=True)
st.markdown("<p class='slogan'>\"Empowering our future, one contribution at a time.\"</p>", unsafe_allow_html=True)

# --- 3. SUBSCRIPTION GATE (The Money Controller) ---
if not st.session_state.sacco['active']:
    st.subheader("🔐 System Activation Required")
    st.write("Monthly Service Fee (Based on Group Size):")
    
    col_tier1, col_tier2, col_tier3 = st.columns(3)
    with col_tier1:
        st.markdown("<div class='card-box'><b>Tier 1 (1-10)</b><br><h3>KES 2,000/mo</h3></div>", unsafe_allow_html=True)
        if st.button("Activate Tier 1"): st.session_state.sacco['active'] = True; st.rerun()
    with col_tier2:
        st.markdown("<div class='card-box'><b>Tier 2 (11-20)</b><br><h3>KES 2,500/mo</h3></div>", unsafe_allow_html=True)
        if st.button("Activate Tier 2"): st.session_state.sacco['active'] = True; st.rerun()
    with col_tier3:
        st.markdown("<div class='card-box'><b>Tier 3 (Up to 30)</b><br><h3>KES 3,500/mo</h3></div>", unsafe_allow_html=True)
        if st.button("Activate Tier 3"): st.session_state.sacco['active'] = True; st.rerun()
    st.stop()

# --- 4. THE PICKER & ELECTION LOGIC ---
if st.session_state.sacco['phase'] == 'Picker':
    st.header("🏗️ Role: The Picker (Setup)")
    st.info("Picker adds members. Role vanishes once the 20-member cap is reached or finalized.")
    
    new_m = st.text_input("Member Name (As per ID/M-Pesa):")
    if st.button("Add Member to Ledger"):
        if len(st.session_state.sacco['members']) < st.session_state.sacco['package_limit']:
            st.session_state.sacco['members'].append(new_m)
            st.success(f"{new_m} added. Current Total: {len(st.session_state.sacco['members'])}")
        else:
            st.error("Limit Reached!")

    if st.button("Start Overseer & Leader Elections"):
        st.session_state.sacco['phase'] = 'Live'
        st.rerun()

# --- 5. THE 3-SIDED MODERN CHAMA SYSTEM ---
else:
    st.sidebar.title("🏢 Navigation")
    side_view = st.sidebar.radio("Switch Dashboard:", ["Member Side", "Chama Side", "M-Pesa Side (Admin)"])
    user_role = st.sidebar.selectbox("Identity Profile:", ["Member", "Chair", "Secretary", "Treasurer", "Overseer"])

    # --- MEMBER SIDE (The Personal Portfolio) ---
    if side_view == "Member Side":
        st.header(f"👤 {user_role} Dashboard")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            # THE LOAN GAUGE (3x Savings)
            limit = st.session_state.sacco['personal_savings'] * 3
            st.markdown(f"<b>📊 Loan Gauge</b> (Limit: KES {limit:,.0f})", unsafe_allow_html=True)
            st.progress(0.15) # 15% used
            st.caption("Usage: KES 5,400 / 36,000")
        with c2:
            # MINI EMERGENCY (3.5% Growth)
            m_emer = st.session_state.sacco['mini_emergency'] * 1.035
            st.metric("Mini-Emergency", f"KES {m_emer:,.2f}", "+3.5% Interest")
        with c3:
            st.metric("Total Personal Savings", f"KES {st.session_state.sacco['personal_savings']:,.0f}")

        st.markdown("---")
        st.subheader("📲 M-Pesa Actions")
        if st.button("Make Contribution (Daily/Weekly/Monthly)"):
            st.success("STK Push Requested. Payout Split: 95% Savings | 5% Chama Fund.")

    # --- CHAMA SIDE (The Collective Wall) ---
    elif side_view == "Chama Side":
        st.header("🏢 Collective Chama Hub")
        
        st.markdown("<div class='card-box'><b>🎯 Monthly Target</b><br>Target: KES 100,000<br>Progress: 68%</div>", unsafe_allow_html=True)
        
        # TRIPLE LOCK EMERGENCY
        st.subheader("🚨 Emergency Protocol")
        st.write("Current Status: <span class='status-badge'>Standby</span>", unsafe_allow_html=True)
        
        if user_role == "Chair":
            if st.button("🔔 Trigger Emergency Notification"):
                st.error("Notification sent to Overseer for Confirmation.")

        # DIVIDEND TRACKER
        st.subheader("📈 Dividend Tracker (5% Retention Growth)")
        st.write("Group Assets (NSE/Land) Value: **KES 480,000**")

    # --- M-PESA SIDE (The Hidden Controller) ---
    elif side_view == "M-Pesa Side (Admin)":
        st.title("🔒 M-Pesa Controller")
        st.error("This is the Safaricom/Developer Backend. Restricted Access.")
        st.write("Monitoring reinvestments and transaction security...")
