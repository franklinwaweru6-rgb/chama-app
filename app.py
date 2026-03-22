import streamlit as st

st.set_page_config(page_title="Chama Dashboard", layout="centered")

st.title("🏛️ Modern Chama Dashboard")

# --- DATA SETTINGS ---
# You can update these numbers later
tax_vault = 20000
n_members = 20
my_contribution = 1500
growth_rate = 1.035  # 3.5% M-Pesa Interest

# --- THE CALCULATIONS (5% - x) ---
x = tax_vault / n_members
base_fund = my_contribution - x
final_emergency_fund = base_fund * growth_rate

# --- DASHBOARD DISPLAY ---
st.markdown(f"### 🛡️ Your Growing Emergency Fund")
st.info(f"Current Value: KES {round(final_emergency_fund, 2)}")

st.markdown("---")
col1, col2 = st.columns(2)
col1.write(f"**Group Fair Share (x):**")
col1.write(f"KES {x}")

col2.write(f"**Your Status:**")
col2.write("3.5% Interest Active ✅")

st.markdown("---")
st.subheader("🚨 Emergency Protocol")
if st.button("TRIGGER EMERGENCY (DEMISE)"):
    st.warning("Action Logged. This will notify the Chair & Overseer immediately.")
    st.write("Next of Kin details have been unlocked for group verification.")
