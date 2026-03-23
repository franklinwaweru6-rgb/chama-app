import streamlit as st
import time

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(page_title="Sisi Sacco Sovereign", layout="wide")

# --- 2. THE SYSTEM STATE (The Brain) ---
if 'app_step' not in st.session_state:
    st.session_state.app_step = "splash"  # Transitions: splash -> terms -> dashboard

if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'roles': {'Chair': 'User_01', 'Secretary': 'User_02', 'Treasurer': 'User_03', 'Overseer': 'User_04'},
        'members': ['Member_01', 'Member_02', 'Member_03', 'Member_04'], # Base +4
        'vault': 1450250.0,
        'stability': 72512.50,
        'logs': ["GENESIS: System Online"],
        'election_pending': False,
        'period': "6-Month",
        'cycle': 1
    }

# --- 3. STAGE 1: THE SPLASH SCREEN (Unity & Loading) ---
if st.session_state.app_step == "splash":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>🤝</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>SISI SACCO SOVEREIGN</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><i>'Umoja ni Nguvu' — Strength in Unity</i></p>", unsafe_allow_html=True)
    
    # Visual Load Simulation
    bar = st.progress(0)
    status_text = st.empty()
    for i in range(1, 101):
        status_text.text(f"Syncing Vault Security... {i}%")
        bar.progress(i)
        time.sleep(0.01) # Smooth fast load
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("PROCEED TO SECURE GATEWAY", use_container_width=True):
        st.session_state.app_step = "terms"
        st.rerun()

# --- 4. STAGE 2: THE TERMS & CONDITIONS ---
elif st.session_state.app_step == "terms":
    st.title("⚖️ Sovereign Protocol Acceptance")
    st.write("Before accessing the Sisi Sacco Vault, you must agree to the operational theory:")
    
    with st.container(border=True):
        st.markdown("""
        **1. Governance:** The $y + 4$ rule is absolute. 4 Leaders + minimum 4 members.
        **2. Inviter Mechanics:** You may invite up to 30 members into your buffer.
        **3. Subscription:** Plans are Bronze, Silver, and Gold based on total headcount.
        **4. Renewal Reset:** Renewal wipes the vault and resets members to start fresh.
        **5. Elections:** A new cycle requires a mandatory leadership re-confirmation.
        """)
    
    agree = st.checkbox("I accept the Sovereign Protocol and the 2/3 Democratic Majority rule.")
    
    if st.button("ENTER VAULT", type="primary"):
        if agree:
            st.session_state.app_step = "dashboard"
            st.rerun()
        else:
            st.error("You must accept the terms to proceed.")

# --- 5. STAGE 3: THE MASTER DASHBOARD ---
elif st.session_state.app_step == "dashboard":
    
    # --- DYNAMIC MATH & THEORY ---
    member_count = len(st.session_state.sacco['members'])
    total_count = 4 + member_count

    # Tiered Logic (Bronze, Silver, Gold)
    if total_count <= 10:
        tier, rate, cap = "🥉 Bronze (Hustler)", 2000, 10
    elif total_count <= 20:
        tier, rate, cap = "🥈 Silver (Standard)", 2500, 20
    else:
        tier, rate, cap = "🥇 Gold (Sovereign)", 3500, 34 # 30 members + 4 leaders

    # Billing Logic (6-Month vs Yearly 10% Discount)
    if st.session_state.sacco['period'] == "Yearly":
        renew_val = (rate * 12) * 0.90
        period_name = "Yearly (10% Discount)"
    else:
        renew_val = rate * 6
        period_name = "6-Month Standard"

    # --- UI LAYOUT ---
    st.title(f"🇰🇪 {tier}")
    st.caption(f"Cycle #{st.session_state.sacco['cycle']} | {period_name}")

    if st.session_state.sacco['election_pending']:
        st.warning("🗳️ MANDATORY ELECTION: New cycle detected. Re-confirm Core Roles (y).")
        if st.button("Confirm Election Results"):
            st.session_state.sacco['sacco']['election_pending'] = False
            st.rerun()

    m1, m2, m3 = st.columns(3)
    m1.metric("Vault Total", f"KES {st.session_state.sacco['vault']:,.0f}")
    m2.metric("Plan Occupancy", f"{total_count}/{cap}")
    m3.metric("Inviter Capacity", f"{member_count}/30")

    st.divider()

    # --- THE THREE TABS ---
    t_port, t_gov, t_audit = st.tabs(["📊 Portfolio", "⚖️ Governance", "📜 Audit Log"])

    with t_port:
        st.subheader("Subscription & Reset Control")
        c1, c2 = st.columns(2)
        with c1:
            choice = st.radio("Switch Plan:", ["6-Month", "Yearly"], 
                              index=0 if st.session_state.sacco['period'] == "6-Month" else 1)
            if choice != st.session_state.sacco['period']:
                st.session_state.sacco['period'] = choice
                st.rerun()
        with c2:
            st.write("**Renewal Total:**")
            st.title(f"KES {renew_val:,.0f}")

        if st.button("🔄 Renew & Reset Everything (Full Restart)", type="primary", use_container_width=True):
            # THE "START ALL OVER" THEORY
            st.session_state.sacco['vault'] = 0.0
            st.session_state.sacco['stability'] = 0.0
            st.session_state.sacco['members'] = ['Member_01', 'Member_02', 'Member_03', 'Member_04']
            st.session_state.sacco['election_pending'] = True
            st.session_state.sacco['cycle'] += 1
            st.session_state.sacco['logs'].append(f"RENEWAL: Cycle {st.session_state.sacco['cycle']} started.")
            st.rerun()

    with t_gov:
        st.subheader("⚖️ y + 4 Security")
        if member_count >= 4:
            st.success("✅ SECURE: Democratic majority is protected.")
        else:
            st.error(f"⚠️ VULNERABLE: Need {4 - member_count} more members.")

        col_l, col_m = st.columns(2)
        with col_l:
            st.write("**Core Roles (y):**")
            for r, u in st.session_state.sacco['roles'].items():
                st.code(f"{r}: {u}")
        with col_m:
            st.write(f"**Member Buffer ({member_count}/30):**")
            for m in st.session_state.sacco['members']:
                mc1, mc2 = st.columns([3, 1])
                mc1.text(m)
                if mc2.button("Exit", key=f"exit_{m}"):
                    st.session_state.sacco['members'].remove(m)
                    st.session_state.sacco['logs'].append(f"EXIT: {m} left.")
                    st.rerun()

    with t_audit:
        for log in reversed(st.session_state.sacco['logs']):
            st.code(log)

    # --- SIDEBAR (INVITER LOGIC) ---
    with st.sidebar:
        st.header("Sacco Admin")
        if st.button("➕ Invite New Member", use_container_width=True):
            # Block if Plan is full OR Inviter Buffer is at 30
            if total_count < cap and member_count < 30:
                new_name = f"Member_{member_count + 1:02d}"
                st.session_state.sacco['members'].append(new_name)
                st.session_state.sacco['logs'].append(f"JOIN: {new_name} added.")
                st.rerun()
            else:
                st.error("Action Blocked: Upgrade Plan or Buffer Full.")
        
        if st.button("🚪 Logout"):
            st.session_state.app_step = "splash"
            st.rerun()
