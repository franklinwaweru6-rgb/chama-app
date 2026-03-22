import streamlit as st
import time

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
        animation: fadeOut 0.5s ease-in-out 8.5s forwards; /* Smooth exit */
    }
    .splash-logo {
        font-size: 5rem; font-weight: 900; letter-spacing: -2px;
        margin-bottom: 5px; animation: fadeIn 2s ease-in;
    }
    .s-red { color: #ef4444; }
    .s-green { color: #10b981; }
    
    /* High-Tech Loader Styling */
    .loader-container {
        display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 40px;
    }
    .loader-bar {
        width: 300px; height: 6px; background: rgba(255,255,255,0.1);
        border-radius: 10px; overflow: hidden;
    }
    .loader-progress {
        width: 0%; height: 100%; background: #10b981; box-shadow: 0 0 20px #10b981;
        animation: loadProgress 4s linear forwards;
    }
    
    @keyframes loadProgress { 0% { width: 0%; } 100% { width: 100%; } }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    @keyframes fadeOut { from { opacity: 1; } to { opacity: 0; visibility: hidden; } }

    /* Main App Reveal Animation */
    .main-app-container { animation: fadeIn 1.5s ease-in; }

    /* Glassmorphic UI Components */
    .vault-card {
        background: white; border-radius: 24px; padding: 30px;
        border-left: 8px solid #10b981;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
    }
    .security-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white; border-radius: 20px; padding: 25px; margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
    }
    .rule-box {
        background: rgba(255,255,255,0.05); border-radius: 15px; padding: 20px;
        border: 1px dashed rgba(255,255,255,0.3); margin-top: 15px; height: 100%;
    }
    .stButton>button {
        width: 100%; border-radius: 50px; height: 3.5rem;
        background: #10b981; color: white !important;
        font-weight: 700; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background: #ef4444; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# --- 2. THE 9-SECOND CINEMATIC SEQUENCER (5s Splash + 4s Load) ---
if 'initialized' not in st.session_state:
    splash_placeholder = st.empty()
    
    # STAGE 1: THE 5-SECOND CINEMATIC BRANDING
    with splash_placeholder.container():
        st.markdown(f"""
            <div class="splash-container">
                <div class="splash-logo"><span class="s-red">S</span>ISI <span class="s-green">SACCO</span></div>
                <p style="font-size: 1.5rem; font-weight: 300; letter-spacing: 3px;">JOINING HANDS FOR A WEALTHIER FUTURE</p>
                <p style="margin-top: 60px; opacity: 0.5; font-size: 0.85rem; letter-spacing: 2px;">"AS WE RISE, WE LEAD"</p>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(5)
    
    # STAGE 2: THE 4-SECOND HIGH-TECH LOAD
    with splash_placeholder.container():
        st.markdown(f"""
            <div class="splash-container">
                <div class="splash-logo" style="font-size: 3rem;"><span class="s-red">S</span>ISI <span class="s-green">SACCO</span></div>
                <div class="loader-container">
                    <div class="loader-bar"><div class="loader-progress"></div></div>
                    <p style="margin-top: 20px; font-family: monospace; color: #10b981; font-size: 0.85rem; letter-spacing: 1px;">
                        VERIFYING y + (4 or more) SECURITY PROTOCOLS...
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(4)
    
    splash_placeholder.empty()
    st.session_state.initialized = True

# --- 3. SYSTEM STATE & CORE LOGIC ---
if 'sacco' not in st.session_state:
    st.session_state.sacco = {
        'total_vault': 1450250.0,
        'stability_pool': 72512.50,
        'reserve_lock': 0.30,
        'satisfaction_rate': 0.88,
        'audit_logs': [
            "SYSTEM: y + (4 or more) Power Balance Verified.",
            "DARAJA: Batch B2C Handshake Successful.",
            "LEGAL: 95/5 Split logic compliant with 2026 Act."
        ]
    }

# --- 4. THE MAIN APPLICATION REVEAL ---
st.markdown("<div class='main-app-container'>", unsafe_allow_html=True)

# Header
col_head, col_badge = st.columns([3, 1])
with col_head:
    st.markdown("<h1><span style='color:#ef4444'>S</span>isi <span style='color:#10b981'>Sacco</span></h1>", unsafe_allow_html=True)
    st.caption("The Sovereign Standard in Digital Group Finance")
with col_badge:
    st.markdown("<div style='text-align:right; margin-top:20px;'><span style='background:#dcfce7; color:#166534; padding:8px 16px; border-radius:30px; font-weight:bold; font-size:12px; border: 1px solid #166534;'>🛡️ VAULT SECURED</span></div>", unsafe_allow_html=True)

# --- 5. THE IMMEDIATE ONBOARDING: y + (4 or more) RULE ---
st.markdown("""
<div class='security-banner'>
    <h2 style='margin-top: 0; color: #10b981;'>⚖️ The Sisi Security Standard</h2>
    <p style='font-size: 1.1rem; opacity: 0.9;'>Before you view your wealth, know how it is protected. This Sacco operates strictly on the <b>y + (4 or more)</b> protocol to guarantee absolute transparency and prevent power monopolies.</p>
    <div style='display: flex; gap: 20px; margin-top: 20px;'>
        <div class='rule-box' style='flex: 1;'>
            <h3 style='color: #ef4444; margin-top: 0;'>y (The 4 Executive Pillars)</h3>
            <p style='opacity: 0.8; font-size: 0.95rem;'>The <b>Chair, Secretary, Treasurer,</b> and <b>Overseer</b>. They facilitate operations but cannot access funds without group consent.</p>
        </div>
        <div class='rule-box' style='flex: 1;'>
            <h3 style='color: #10b981; margin-top: 0;'>+ (4 or more) Members</h3>
            <p style='opacity: 0.8; font-size: 0.95rem;'>The infinite buffer of regular members. You hold the ultimate <b>2/3 Voting Power</b> to retain or replace leadership at any time.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. FINANCIAL DASHBOARD ---
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Group Savings (95%)", f"KES {st.session_state.sacco['total_vault']:,.0f}", "Fortress Mode")
with m2:
    st.metric("Stability Vault (5%)", f"KES {st.session_state.sacco['stability_pool']:,.2f}", "Loan Source")
with m3:
    st.metric("Yield Rate", "3.5%", "Daily Accrual")

# --- 7. ACTION NAVIGATION TABS ---
t1, t2, t3 = st.tabs(["👤 My Wallet", "🏢 Governance", "🔒 Sovereign Audit"])

with t1:
    st.markdown("<div class='vault-card'>", unsafe_allow_html=True)
    st.subheader("Asset Breakdown")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.metric("My Mini-Emergency Fund", "KES 14,250", "Available instantly")
    with col_w2:
        st.write("**Loan Eligibility (3x Savings Limit)**")
        st.progress(0.15, text="Limit: KES 360,000")
    
    if st.button("🚀 Apply for Stability Loan"):
        st.toast("Verifying Social Collateral Protocol...")
    st.markdown("</div>", unsafe_allow_html=True)

with t2:
    st.header("The 2/3 Satisfaction Valve")
    st.info("The executive leaders remain in power ONLY while 66.7% of the total y + (4 or more) group is satisfied.")
    
    sat_val = st.session_state.sacco['satisfaction_rate']
    st.progress(sat_val, text=f"Current Consensus: {sat_val*100:.1f}%")
    
    if st.button("❌ Request Leadership Review (Anonymous)"):
        st.warning("Dissent recorded. If 1/3 of members agree, mandatory elections will be triggered.")

with t3:
    st.header("Immutable Ledger Logs")
    for log in reversed(st.session_state.sacco['audit_logs']):
        st.code(f"> {log}", language="bash")
    if st.button("💰 Distribute End-of-Cycle Funds"):
        st.balloons()
        st.success("B2C API Handshake: 95/5 Split processed for all members.")

st.markdown("</div>", unsafe_allow_html=True) # End main app container
