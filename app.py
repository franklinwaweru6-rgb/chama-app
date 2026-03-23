import streamlit as st

# --- 1. CORE SACCO DATA & HIERARCHY (The y + 4 Rule) ---
# 'y' = 4 Leaders | '+4' = Base Members | Max = 30 Members
if 'sacco_data' not in st.session_state:
    st.session_state.sacco_data = {
        'leaders': ['Chair', 'Secretary', 'Treasurer', 'Overseer'],
        'members': ['Member_01', 'Member_02', 'Member_03', 'Member_04'], # The base +4
        'vault_total': 1450250.0,
        'stability_pool': 72512.50,
        'audit_logs': ["SYSTEM: Genesis Block Verified", "SECURITY: y+4 Rule Active"]
    }

# --- 2. CALCULATE GROUP SPECS ---
total_people = len(st.session_state.sacco_data['leaders']) + len(st.session_state.sacco_data['members'])
member_count = len(st.session_state.sacco_data['members'])

# Determine the Plan Tier based on total people
if total_people <= 10:
    current_plan = "Tier 1 (Starter)"
    monthly_cost = 2000
elif total_people <= 20:
    current_plan = "Tier 2 (Growth)"
    monthly_cost = 2500
else:
    current_plan = "Tier 3 (Pro)"
    monthly_cost = 3500

# --- 3. UI LAYOUT ---
st.title("🇰🇪 Sisi Sacco: Sovereign Dashboard")
st.markdown(f"**Current Plan:** {current_plan} | **System Status:** Online")

# Metrics Row
m1, m2, m3 = st.columns(3)
m1.metric("Group Savings", f"KES {st.session_state.sacco_data['vault_total']:,.0f}")
m2.metric("Stability Vault", f"KES {st.session_state.sacco_data['stability_pool']:,.2f}")
m3.metric("Total Members", f"{total_people}/34") # 4 leaders + 30 max members

# --- 4. THE CORRECT TAB LOGIC (Line 188 Fix) ---
t1, t2, t3 = st.tabs(["📊 Portfolio", "⚖️ Governance", "📜 Audit Log"])

with t1:
    st.subheader("Vault Breakdown")
    st.write(f"Your group is currently on the **{current_plan}** plan.")
    st.info(f"Monthly Subscription: KES {monthly_cost:,}")
    
    # Progress bar towards the 30-member inviter limit
    progress = member_count / 30
    st.write(f"Inviter Progress: {member_count} / 30 members added")
    st.progress(progress)

with t2:
    st.subheader("⚖️ y + 4 Security Protocol")
    
    # Democratic Check
    if member_count >= 4:
        st.success("✅ SECURITY: SAFE. 2/3 Majority requires independent member votes.")
    else:
        st.error(f"⚠️ VULNERABLE: Need {4 - member_count} more members to satisfy y+4 rule.")

    st.write("---")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Core Leaders (y):**")
        for leader in st.session_state.sacco_data['leaders']:
            st.code(leader)
    with col_b:
        st.write(f"**Buffer Members ({member_count}/30):**")
        st.write(st.session_state.sacco_data['members'])

with t3:
    st.subheader("Immutable Audit Trail")
    for log in st.session_state.sacco_data['audit_logs']:
        st.text(f"ID_{log.split(':')[0]} >> {log}")

# --- 5. ACTION SIDEBAR ---
with st.sidebar:
    st.header("Sacco Actions")
    if st.button("Simulate New Member Invite"):
        if member_

