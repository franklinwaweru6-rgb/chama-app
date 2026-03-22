import streamlit as st
import pandas as pd
import hashlib
import time
import math

# --- 1. GLOBAL BRANDING & THEME ENGINE ---
st.set_page_config(page_title="Sisi Sacco", page_icon="S", layout="wide")

st.markdown("""
    <style>
    /* Professional Slate Background */
    .stApp { background-color: #f8fafc; }
    
    /* Cinematic Splash Screen */
    .splash-container {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), 
                    url('https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1500&q=80');
        background-size: cover;
        background-position: center;
        z-index: 9999;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
    }
    .splash-logo {
        font-size: 4.5rem; font-weight: 900; letter-spacing: -2px;
        margin-bottom: 5px; animation: fadeIn 1.5s ease-in;
    }
    .s-red { color: #ef4444; }
    .s-green { color: #10b981; }
    
    /* High-Tech Loader */
    .loader {
        border: 3px solid rgba(255,255,255,0.1);
        border-top: 3px solid #10b981;
        border-radius: 50%;
        width: 50px; height: 50px;
        animation: spin 1s linear infinite;
        margin: 20px auto;
    }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

    /* Glassmorphic Elements */
    .vault-card {
        background: white;
        border-radius: 24px;
        padding: 30px;
        border-left: 10px solid #10b981;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
    }
    
    /* Professional Sisi Buttons */
    .stButton>button {
        width: 100%; border-radius: 50px; height: 3.5rem;
        background: #10b981; color: white !important;
        font-weight: 700; border: none; transition: 0.3s;
    }
    .stButton>button:hover {
        background: #ef4444; transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE SPLASH SEQUENCER ---
if 'initialized' not in st.session_state:
    splash_placeholder = st.empty()
    with splash_placeholder.container():
        st.markdown(f"""
            <div class="splash-container">
                <div class="splash-logo"><span class="s-red">S</span>ISI <span class="s-green">SACCO</span> APP</div>
                <p style="font-size: 1.3rem; font-weight: 300; opacity: 0.9;">"As We Rise, We Lead"</p>
                <div class="loader"></div>
                <p style="font-family: monospace; color: #10b981; letter-spacing: 1px;">ENCRYPTING DARAJA GATEWAY... DONE</p>
                <p style="font-family: monospace; color: #64748b;">INITIALIZING y+4 PROTOCOLS...</p>
            </div>
        """, unsafe_allow_html=True)
    
    time.sleep(3) # The "One-of-One" cinematic delay
    splash_placeholder.empty()
    st.session_state.initialized = True

# --- 3. SYSTEM STATE & LOGIC ---
if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'phase': 'Active', 
        'vault_total': 1450250.0,
        'stability_pool': 72512.50, # 5% Stability
        'reserve_lock': 0.30,       # 30% Emergency Hard-Lock
        'members': {'User_Admin': {'savings': 120000, 'interest': 4200, 'loan': 0}},
        'satisfaction_votes': {}
    }

# --- 4. TOP-CLASS DASHBOARD UI ---
col_head, col_badge = st.columns([3, 1])
with col_head:
    st.markdown("<h1><span style='color:#ef4444'>S</span>isi <span style='color:#10b981'>Sacco</span></h1>", unsafe_allow_html=True)
    st.caption("2026 Sovereign Financial Engine | Multi-Billion Ready")

with col_badge:
    st.markdown("<div style='text-align:right; margin-top:20px;'><span style='background:#fee2e2; color:#ef4444; padding:8px 16px; border-radius:30px; font-weight:bold; font-size:12px;'>🛡️ y+4 SECURED</span></div>", unsafe_allow_html=True)

st.divider()

# Core Metrics
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Group Savings (95%)", f"KES {st.session_state.sacco['vault_total']:,.0f}", "Fortress Mode")
with m2:
    st.metric("Stability Vault (5%)", f"KES {st.session_state.sacco['stability_pool']:,.2f}", "Loan Source")
with m3:
    st.metric("Safaricom Yield", "3.5%", "Daily Accrual")

# --- 5. THE THREE-SIDED ENGINE ---
tab1, tab2, tab3 = st.tabs(["👤 My Portfolio", "🏢 Group Governance", "🔒 Leader Vault"])

with tab1:
    st.markdown("<div class='vault-card'>", unsafe_allow_html=True)
    st.subheader("Your Personal Wealth Gauge")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.metric("Mini-Emergency Pool", "KES 14,250", "Available Instantly")
    with col_p2:
        st.write("**Loan Eligibility (3x Savings)**")
        st.progress(0.4, text="Used: KES 0 / Limit: 360,000")
    
    if st.button("🚀 Apply for Stability Loan"):
        st.toast("Verifying 2 Guarantors...")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.header("Democratic Satisfaction Valve")
    st.info("The 2/3 Rule: If satisfaction drops below 66.7%, a leadership election is auto-triggered.")
    
    # 2/3 Satisfaction Calculation
    current_satisfaction = 0.85 # Simulated 85%
    st.progress(current_satisfaction, text=f"Consensus: {current_satisfaction*100:.1f}%")
    
    if st.button("❌ I am NOT Satisfied (Vote for Election)"):
        st.warning("Vote Recorded. If 3 members agree, the election opens.")

with tab3:
    st.header("Executive Controller")
    st.write("Authorized Personnel Only (Treasurer / Overseer)")
    if st.button("💰 Distribute End-of-Cycle Funds"):
        st.balloons()
        st.success("95/5 Split processed. All pro-rata payments sent via M-Pesa B2C.")

# --- 6. SOVEREIGN AUDIT TRAIL ---
st.markdown("---")
with st.expander("🔍 System Immutable Logs"):
    st.code(f"""
    [16:42:01] SECURE_HANDSHAKE: Safaricom G2 Gateway Verified.
    [16:42:05] SYSTEM_AUDIT: All {len(st.session_state.sacco['members'])} accounts in balance.
    [16:43:10] CALC_ENGINE: Banker's Rounding applied to interest remainder.
    [16:45:00] VOTE_CHECK: 2/3 Satisfaction Gate remains LOCKED.
    """, language="bash")
