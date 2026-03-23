import streamlit as st
import time

# --- 1. SYSTEM CONFIG ---
st.set_page_config(page_title="Sisi Sacco Sovereign", layout="wide")

# --- 2. SESSION STATE INITIALIZATION ---
if 'app_state' not in st.session_state:
    st.session_state.app_state = "splash"  # States: splash, terms, dashboard

if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'roles': {'Chair': 'User_01', 'Secretary': 'User_02', 'Treasurer': 'User_03', 'Overseer': 'User_04'},
        'members': ['Member_01', 'Member_02', 'Member_03', 'Member_04'],
        'vault_balance': 1450250.0,
        'audit_trail': ["GENESIS: Sisi Sacco Protocol Initialized"],
        'is_election_phase': False,
        'billing_cycle': "6-Month",
        'current_cycle': 1
    }

# --- 3. THE SPLASH SCREEN ---
if st.session_state.app_state == "splash":
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🇰🇪 SISI SACCO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Securing the Future of Group Savings</p>", unsafe_allow_html=True)
    
    # Simple progress bar to simulate loading
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    if st.button("Enter Application", use_container_width=True):
        st.session_state.app_state = "terms"
        st.rerun()

# --- 4. TERMS & CONDITIONS GATE ---
elif st.session_state.app_state == "terms":
    st.title("⚖️ Terms of Service")
    st.info("Please review the Sisi Sacco Sovereign Protocol rules before entering.")
    
    with st.expander("Read Full Terms & Conditions"):
        st.write("""
        1. **Security:** This app operates on the y+4 democratic principle.
        2. **Financials:** Subscription tiers are Bronze (Hustler), Silver (Standard), and Gold (Sovereign).
        3. **Renewals:** Subscription renewal triggers a mandatory leadership election and financial reset.
        4. **Governance:** Members have the right to exit the Chama at any time, subject to group audit.
        """)
    
    agree = st.checkbox("I accept the Sisi Sacco Sovereign Protocol and the y+4 Governance Rule.")
    
    if st.button("Proceed to Dashboard"):
        if agree:
            st.session_state.app_state = "dashboard"
            st.rerun()
        else:
            st.warning("You must accept the terms to continue.")

# --- 5. THE MAIN MASTER DASHBOARD ---
elif st.session_state.app_state == "dashboard":
    
    # --- DYNAMIC LOGIC ---
    member_count = len(st.session_state.sacco['members'])
    total_headcount = 4 + member_count

    # Tier Pricing Theory
    if total_headcount <= 10:
        plan_name, monthly_rate, plan_limit = "🥉 Bronze (Hustler)", 2000, 10
    elif total_headcount <= 20:
        plan_name, monthly_rate, plan_limit = "🥈 Silver (Standard)", 2500, 20
    else:
        plan_name, monthly_rate, plan_limit = "🥇 Gold (Sovereign)", 3500, 34 

    # Billing Mode Theory
    if st.session_state.sacco['billing_cycle'] == "Yearly":
        renewal_cost = (monthly_rate * 12) * 0.90
        cycle_label = "Yearly (10% Discount)"
    else:
        renewal_cost = monthly_rate * 6
        cycle_label = "Standard 6-Month"

    # --- UI LAYOUT ---
    st.title("🇰🇪 Sisi Sacco: Sovereign Dashboard")
    st.caption(f"Package: {plan_name} | Cycle: {st.session_state.sacco['current_cycle']}")

    # Mandatory Election Overlay
    if st.session_state.sacco['is_election_phase']:
        st.warning("🗳️ ELECTION REQUIRED: Please re-validate Core Roles for the new cycle.")
        if st.button("Confirm Election Completion"):
            st.session_state.sacco['is_election_phase'] = False
            st.rerun()

    m1, m2, m3 = st.columns(3)
    m1.metric("Vault Total", f"KES {st.session_state.sacco['vault_balance']:,.0f}")
    m2.metric("Plan Occupancy", f"{total_headcount}/{plan_limit}")
    m3.metric("Inviter Buffer", f"{member_count}/30")

    st.divider()

    # --- TABS ---
    tab_port, tab_gov, tab_audit = st.tabs(["📊 Portfolio", "⚖️ Governance", "📜 Audit Log"])

    with tab_port:
        st.subheader("Subscription & Reset")
        col_a, col_b = st.columns(2)
        with col_a:
            mode = st.radio("Select Billing Mode:", ["6-Month", "Yearly"], 
                            index=0 if st.session_state.sacco['billing_cycle'] == "6-Month" else 1)
            if mode != st.session_state.sacco['billing_cycle']:
                st.session_state.sacco['billing_cycle'] = mode
                st.rerun()
        with col_b:
            st.write("**Next Renewal Amount:**")
            st.title(f"KES {renewal_cost:,.0f}")

        if st.button("🔄 Renew & Reset Cycle", type="primary", use_container_width=True):
            # FULL RESET THEORY: Wipes money, resets members, starts over
            st.session_state.sacco['vault_balance'] = 0.0
            st.session_state.sacco['members'] = ['Member_01', 'Member_02', 'Member_03', 'Member_04']
            st.session_state.sacco['is_election_phase'] = True
            st.session_state.sacco['current_cycle'] += 1
            st.session_state.sacco['audit_trail'].append(f"RENEWAL: Cycle {st.session_state.sacco['current_cycle']} started.")
            st.rerun()

    with tab_gov:
        st.subheader("⚖️ y + 4 Governance")
        if member_count >= 4:
            st.success("✅ SECURE: Democratic majority is active.")
        else:
            st.error(f"⚠️ VULNERABLE: Need {4 - member_count} more members.")

        g_l, g_m = st.columns(2)
        with g_l:
            st.write("**Core Roles (y):**")
            for r, n in st.session_state.sacco['roles'].items():
                st.code(f"{r}: {n}")
        with g_m:
            st.write(f"**Member Buffer ({member_count}/30):**")
            for m in st.session_state.sacco['members']:
                mc1, mc2 = st.columns([4, 1])
                mc1.text(m)
                if mc2.button("Exit", key=f"exit_{m}"):
                    st.session_state.sacco['members'].remove(m)
                    st.session_state.sacco['audit_trail'].append(f"EXIT: {m} left.")
                    st.rerun()

    with tab_audit:
        for log in reversed(st.session_state.sacco['audit_trail']):
            st.text(f"LOG >> {log}")

    # --- SIDEBAR ---
    with st.sidebar:
        st.header("Admin")
        if st.button("➕ Add Member", use_container_width=True):
            if total_headcount < plan_limit and member_count < 30:
                new_id = f"Member_{member_count + 1:02d}"
                st.session_state.sacco['members'].append(new_id)
                st.session_state.sacco['audit_trail'].append(f"JOIN: {new_id} added.")
                st.rerun()
            else:
                st.error("Cannot add: Plan Full or Max limit reached.")
        
        if st.button("🚪 Logout"):
            st.session_state.app_state = "splash"
            st.rerun()
