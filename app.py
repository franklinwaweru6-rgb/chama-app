import streamlit as st
import time

# --- 1. GLOBAL SYSTEM CONFIG ---
st.set_page_config(page_title="Sisi Sacco Sovereign", layout="wide", initial_sidebar_state="collapsed")

# --- 2. THE BRAIN (Session State) ---
if 'app_step' not in st.session_state:
    st.session_state.app_step = "splash"  # Sequence: splash -> terms -> dashboard

if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'roles': {'Chair': 'User_01', 'Secretary': 'User_02', 'Treasurer': 'User_03', 'Overseer': 'User_04'},
        'members': ['Member_01', 'Member_02', 'Member_03', 'Member_04'], # Base +4
        'vault': 1450250.0,
        'stability': 72512.50,
        'logs': ["GENESIS: System Secured"],
        'election_pending': False,
        'period': "6-Month",
        'cycle': 1
    }

# --- 3. STAGE 1: THE VISUAL SPLASH SCREEN ---
if st.session_state.app_step == "splash":
    st.markdown("<br>", unsafe_allow_html=True)
    # Visual Unity Image (Holding Hands)
    st.image("https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1200&q=80", 
             caption="Umoja ni Nguvu — Sisi Sacco Sovereign")
    
    st.markdown("<h1 style='text-align: center; color: #1B5E20;'>SISI SACCO</h1>", unsafe_allow_html=True)
    
    # Progress Bar Simulation
    progress_bar = st.progress(0)
    status = st.empty()
    for i in range(1, 101):
        status.markdown(f"<p style='text-align: center;'>Syncing Secure Vault... {i}%</p>", unsafe_allow_html=True)
        progress_bar.progress(i)
        time.sleep(0.02)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("PROCEED TO GATEWAY", use_container_width=True):
        st.session_state.app_step = "terms"
        st.rerun()

# --- 4. STAGE 2: TERMS & CONDITIONS GATE ---
elif st.session_state.app_step == "terms":
    st.title("⚖️ Sovereign Protocol & T&Cs")
    st.write("To protect the Sacco, you must accept the following terms:")
    
    with st.container(border=True):
        st.markdown("""
        - **$y + 4$ Protocol:** 4 Leaders + minimum 4 members are required for democratic safety.
        - **Inviter Rule:** You may invite up to 30 members total in your buffer.
        - **Tiered Plans:** 🥉 Bronze (1-10), 🥈 Silver (11-20), 🥇 Gold (21-34).
        - **Renewal Logic:** Subscription renewal wipes the vault and resets members to start fresh.
        - **Mandatory Elections:** New cycles require re-confirmation of the 4 Core Roles.
        """)
    
    agree = st.checkbox("I accept the Sovereign Protocol and the 2/3 Democratic Majority rule.")
    
    if st.button("ENTER VAULT", type="primary", use_container_width=True):
        if agree:
            st.session_state.app_step = "dashboard"
            st.rerun()
        else:
            st.error("Protocol acceptance is mandatory for entry.")

# --- 5. STAGE 3: THE MASTER DASHBOARD ---
elif st.session_step == "dashboard" or st.session_state.app_step == "dashboard":
    
    # --- DYNAMIC CALCULATIONS ---
    member_count = len(st.session_state.sacco['members'])
    total_count = 4 + member_count

    # Plan Tiers
    if total_count <= 10:
        tier, rate, cap = "🥉 Bronze (Hustler)", 2000, 10
    elif total_count <= 20:
        tier, rate, cap = "🥈 Silver (Standard)", 2500, 20
    else:
        tier, rate, cap = "🥇 Gold (Sovereign)", 3500, 34 

    # Billing (6m vs Yearly 10% Off)
    if st.session_state.sacco['period'] == "Yearly":
        renew_val = (rate * 12) * 0.90
        p_label = "Yearly (10% Discount)"
    else:
        renew_val = rate * 6
        p_label = "6-Month Standard"

    # --- UI LAYOUT ---
    st.title(f"🇰🇪 {tier}")
    st.caption(f"Cycle #{st.session_state.sacco['cycle']} | {p_label}")

    if st.session_state.sacco['election_pending']:
        st.warning("🗳️ ELECTION REQUIRED: Re-validate Core Roles for the new cycle.")
        if st.button("Confirm Election Completion"):
            st.session_state.sacco['election_pending'] = False
            st.rerun()

    m1, m2, m3 = st.columns(3)
    m1.metric("Vault Total", f"KES {st.session_state.sacco['vault']:,.0f}")
    m2.metric("Plan Capacity", f"{total_count}/{cap}")
    m3.metric("Inviter Buffer", f"{member_count}/30")

    st.divider()

    # --- TABS ---
    t_port, t_gov, t_audit = st.tabs(["📊 Portfolio", "⚖️ Governance", "📜 Audit Log"])

    with t_port:
        st.subheader("Subscription Control")
        c1, c2 = st.columns(2)
        with c1:
            choice = st.radio("Cycle:", ["6-Month", "Yearly"], 
                              index=0 if st.session_state.sacco['period'] == "6-Month" else 1)
            if choice != st.session_state.sacco['period']:
                st.session_state.sacco['period'] = choice
                st.rerun()
        with c2:
            st.write("**Total for Renewal:**")
            st.title(f"KES {renew_val:,.0f}")

        if st.button("🔄 Renew & Reset Everything (Full Restart)", type="primary", use_container_width=True):
            # THE "START ALL OVER" LOGIC
            st.session_state.sacco['vault'] = 0.0
            st.session_state.sacco['members'] = ['Member_01', 'Member_02', 'Member_03', 'Member_04']
            st.session_state.sacco['election_pending'] = True
            st.session_state.sacco['cycle'] += 1
            st.session_state.sacco['logs'].append(f"RENEWAL: Cycle {st.session_state.sacco['cycle']} started.")
            st.rerun()

    with t_gov:
        st.subheader("⚖️ y + 4 Security")
        if member_count >= 4:
            st.success("✅ DEMOCRATICALLY SECURE")
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
                    st.session_state.sacco['logs'].append(f"EXIT: {m} removed.")
                    st.rerun()

    with t_audit:
        for log in reversed(st.session_state.sacco['logs']):
            st.code(log)

    # --- SIDEBAR (INVITER) ---
    with st.sidebar:
        st.header("Admin")
        if st.button("➕ Invite New Member", use_container_width=True):
            if total_count < cap and member_count < 30:
                new_name = f"Member_{member_count + 1:02d}"
                st.session_state.sacco['members'].append(new_name)
                st.session_state.sacco['logs'].append(f"JOIN: {new_name} added.")
                st.rerun()
            else:
                st.error("Upgrade Plan or Max Inviter limit reached.")
        
        if st.button("🚪 Logout"):
            st.session_state.app_step = "splash"
            st.rerun()
