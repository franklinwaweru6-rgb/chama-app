import streamlit as st

# --- 1. CORE SYSTEM CONFIG ---
st.set_page_config(page_title="Sisi Sacco Master", layout="wide", initial_sidebar_state="expanded")

# --- 2. THE FOUNDATIONAL THEORY (Initialization) ---
# y = 4 Core Leaders (Chair, Secretary, Treasurer, Overseer)
# +4 = Base independent members required for a 2/3 democratic majority
if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'roles': {
            'Chair': 'Leader_01',
            'Secretary': 'Leader_02',
            'Treasurer': 'Leader_03',
            'Overseer': 'Leader_04'
        },
        'members': ['Member_01', 'Member_02', 'Member_03', 'Member_04'], 
        'vault_balance': 1450250.0,
        'audit_trail': ["GENESIS: Sisi Sacco Protocol Initialized", "SECURITY: y+4 Rule Active"],
        'is_election_phase': False,
        'billing_cycle': "6-Month",
        'current_cycle': 1
    }

# --- 3. DYNAMIC THEORY CALCULATIONS ---
member_count = len(st.session_state.sacco['members'])
total_headcount = 4 + member_count  # Leaders (y) + Members

# THE THREE-TIERED PRICING PLANS (As per your theory)
if total_headcount <= 10:
    plan_name, monthly_rate, plan_limit = "🥉 Bronze (Hustler)", 2000, 10
elif total_headcount <= 20:
    plan_name, monthly_rate, plan_limit = "🥈 Silver (Standard)", 2500, 20
else:
    # Max is 30 members + 4 leaders = 34
    plan_name, monthly_rate, plan_limit = "🥇 Gold (Sovereign)", 3500, 34 

# THE TWO MAJOR SUBSCRIPTION MODES
if st.session_state.sacco['billing_cycle'] == "Yearly":
    # 12 Months with 10% Discount
    renewal_cost = (monthly_rate * 12) * 0.90
    cycle_label = "Yearly Plan (10% Discount Applied)"
else:
    # Standard 6-Month Block
    renewal_cost = monthly_rate * 6
    cycle_label = "Standard 6-Month Plan"

# --- 4. THE RENEWAL & RESET LOGIC ---
def execute_full_renewal():
    """Theory: After renewal, it starts all over again."""
    st.session_state.sacco['vault_balance'] = 0.0
    # Reset members back to the base +4 buffer
    st.session_state.sacco['members'] = ['Member_01', 'Member_02', 'Member_03', 'Member_04']
    st.session_state.sacco['is_election_phase'] = True
    st.session_state.sacco['current_cycle'] += 1
    st.session_state.sacco['audit_trail'].append(f"RENEWAL: Cycle {st.session_state.sacco['current_cycle']} started. All progress reset.")

# --- 5. MAIN INTERFACE ---
st.title("🇰🇪 Sisi Sacco: Sovereign System")
st.markdown(f"**Current Package:** {plan_name} | **Billing:** {cycle_label}")

# MANDATORY ELECTION CHECK
if st.session_state.sacco['is_election_phase']:
    st.error("🗳️ MANDATORY ELECTION: Subscription renewed. Roles must be re-validated.")
    if st.button("Confirm Election Completion"):
        st.session_state.sacco['is_election_phase'] = False
        st.rerun()

# TOP-LEVEL METRICS
col1, col2, col3 = st.columns(3)
col1.metric("Vault Total", f"KES {st.session_state.sacco['vault_balance']:,.2f}")
col2.metric("People in Plan", f"{total_headcount}/{plan_limit}")
col3.metric("Inviter Buffer", f"{member_count}/30", help="Max buffer is 30 members")

st.divider()

# --- 6. THE THREE TABS (Portfolio, Governance, Audit) ---
tab_port, tab_gov, tab_audit = st.tabs(["📊 Portfolio", "⚖️ Governance", "📜 Audit Log"])

with tab_port:
    st.subheader("Subscription & Financials")
    c1, c2 = st.columns(2)
    with c1:
        # Toggle between the two major plans
        mode = st.radio("Change Cycle:", ["6-Month", "Yearly"], 
                        index=0 if st.session_state.sacco['billing_cycle'] == "6-Month" else 1)
        if mode != st.session_state.sacco['billing_cycle']:
            st.session_state.sacco['billing_cycle'] = mode
            st.rerun()
    with c2:
        st.write("**Next Renewal Amount:**")
        st.title(f"KES {renewal_cost:,.0f}")

    if st.button("🔄 Renew & Reset (Start New Cycle)", type="primary", use_container_width=True):
        execute_full_renewal()
        st.rerun()

with tab_gov:
    st.subheader("⚖️ y + 4 Governance Protocol")
    
    # Democratic Guardrail
    if member_count >= 4:
        st.success("✅ DEMOCRATICALLY SECURE: Leader power is checked by members.")
    else:
        st.error(f"⚠️ VULNERABLE: Need {4 - member_count} more members for y+4 base.")

    g_roles, g_mems = st.columns(2)
    with g_roles:
        st.write("**Core Roles (y):**")
        for role, name in st.session_state.sacco['roles'].items():
            st.code(f"{role}: {name}")
    with g_mems:
        st.write(f"**Member Buffer ({member_count}/30):**")
        for m in st.session_state.sacco['members']:
            mc1, mc2 = st.columns([4, 1])
            mc1.text(m)
            # MEMBER EXIT LOGIC
            if mc2.button("Exit", key=f"exit_{m}"):
                st.session_state.sacco['members'].remove(m)
                st.session_state.sacco['audit_trail'].append(f"EXIT: {m} has left the Sacco.")
                st.rerun()

with tab_audit:
    st.subheader("System Logs")
    for log in reversed(st.session_state.sacco['audit_trail']):
        st.text(f"LOG >> {log}")

# --- 7. SIDEBAR ACTIONS (The Inviter Logic) ---
with st.sidebar:
    st.header("Admin Controls")
    # ADDITION LOGIC: Check plan limit AND 30-member buffer limit
    if st.button("➕ Add Member to Chama", use_container_width=True):
        if total_headcount < plan_limit:
            if member_count < 30:
                new_mem = f"Member_{member_count + 1:02d}"
                st.session_state.sacco['members'].append(new_mem)
                st.session_state.sacco['audit_trail'].append(f"JOIN: {new_mem} added by Inviter.")
                st.rerun()
            else:
                st.error("Inviter max (30) reached.")
        else:
            st.error(f"Plan Full! Current {plan_name} only allows {plan_limit} people.")
    
    st.divider()
    st.caption("Sisi Sacco Tech v4.2 | 2026")
