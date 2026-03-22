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
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), 
                    url('https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1500&q=80');
        background-size: cover; background-position: center; z-index: 9999;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        color: white; text-align: center;
        animation: fadeOut 0.5s ease-in-out 8.5s forwards;
    }
    .splash-logo { font-size: 5rem; font-weight: 900; letter-spacing: -2px; margin-bottom: 5px; animation: fadeIn 2s ease-in; }
    .s-red { color: #ef4444; } .s-green { color: #10b981; }
    
    /* Loaders & Animations */
    .loader-container { display: flex; flex-direction: column; align-items: center; margin-top: 40px; }
    .loader-bar { width: 300px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; }
    .loader-progress { width: 0%; height: 100%; background: #10b981; box-shadow: 0 0 20px #10b981; animation: loadProgress 4s linear forwards; }
    @keyframes loadProgress { 0% { width: 0%; } 100% { width: 100%; } }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    @keyframes fadeOut { from { opacity: 1; } to { opacity: 0; visibility: hidden; } }

    /* UI Components */
    .vault-card {
        background: white; border-radius: 24px; padding: 30px;
        border-left: 8px solid #10b981; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05); margin-bottom: 25px;
    }
    .plan-card {
        background: white; border-radius: 20px; padding: 25px; text-align: center;
        border: 2px solid #e2e8f0; transition: all 0.3s ease; height: 100%;
    }
    .plan-card:hover { border-color: #10b981; transform: translateY(-5px); box-shadow: 0 15px 30px -5px rgba(16, 185, 129, 0.2); }
    .security-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white;
        border-radius: 20px; padding: 25px; margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%; border-radius: 50px; height: 3.5rem; background: #10b981; color: white !important;
        font-weight: 700; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background: #ef4444; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# --- 2. STATE ROUTER (THE TOP-TO-BOTTOM ENGINE) ---
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'splash'
if 'sacco' not in st.session_state:
    st.session_state.sacco = { 'total_vault': 1450250.0, 'stability_pool': 72512.50, 'satisfaction_rate': 0.88, 'audit_logs': [] }

# --- 3. PHASE 0: THE CINEMATIC SPLASH ---
if st.session_state.app_state == 'splash':
    splash_placeholder = st.empty()
    with splash_placeholder.container():
        st.markdown(f"""
            <div class="splash-container">
                <div class="splash-logo"><span class="s-red">S</span>ISI <span class="s-green">SACCO</span></div>
                <p style="font-size: 1.5rem; font-weight: 300; letter-spacing: 3px;">JOINING HANDS FOR A WEALTHIER FUTURE</p>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(5)
    with splash_placeholder.container():
        st.markdown(f"""
            <div class="splash-container">
                <div class="splash-logo" style="font-size: 3rem;"><span class="s-red">S</span>ISI <span class="s-green">SACCO</span></div>
                <div class="loader-container">
                    <div class="loader-bar"><div class="loader-progress"></div></div>
                    <p style="margin-top: 20px; font-family: monospace; color: #10b981; font-size: 0.85rem;">LOADING PROTOCOLS...</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(4)
    splash_placeholder.empty()
    st.session_state.app_state = 'step_1_security'
    st.rerun()

# --- 4. PHASE 1: THE LAW (y + 4/more) ---
if st.session_state.app_state == 'step_1_security':
    st.markdown("<h1><span class='s-red'>S</span>isi <span class='s-green'>Sacco</span> Onboarding</h1>", unsafe_allow_html=True)
    st.progress(0.25, text="Step 1 of 4: The Sovereign Security Law")
    
    st.markdown("""
    <div class='security-banner'>
        <h2 style='margin-top: 0; color: #10b981;'>⚖️ The y + (4 or more) Security Standard</h2>
        <p style='font-size: 1.1rem;'>Before entering your details, you must understand our absolute rule of transparency.</p>
        <div style='background: rgba(255,255,255,0.05); border-radius: 15px; padding: 20px; border: 1px dashed rgba(255,255,255,0.3);'>
            <h3 style='color: #ef4444; margin-top: 0;'>y (The 4 Executive Pillars)</h3>
            <p>Chair, Secretary, Treasurer, and Overseer facilitate operations but hold no dictatorial power.</p>
            <h3 style='color: #10b981; margin-top: 15px;'>+ (4 or more) Independent Members</h3>
            <p>You and the other members hold the 2/3 Voting Power. No funds move without majority consensus.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("I Agree to the y + (4 or more) Protocol"):
        st.session_state.app_state = 'step_2_member'
        st.rerun()

# --- 5. PHASE 2: MEMBER IDENTITY ---
elif st.session_state.app_state == 'step_2_member':
    st.markdown("<h1><span class='s-red'>S</span>isi <span class='s-green'>Sacco</span> Onboarding</h1>", unsafe_allow_html=True)
    st.progress(0.50, text="Step 2 of 4: Digital Identity Verification")
    
    st.markdown("<div class='vault-card'>", unsafe_allow_html=True)
    st.subheader("👤 Create Your Digital Vault Profile")
    member_name = st.text_input("Full Legal Name (As per ID):")
    member_phone = st.text_input("Safaricom M-Pesa Number:", placeholder="07XX XXX XXX")
    
    if st.button("Verify Identity via Daraja API"):
        if member_name and member_phone:
            st.session_state.member_name = member_name
            st.session_state.app_state = 'step_3_plans'
            st.rerun()
        else:
            st.error("Please enter your name and M-Pesa number to proceed.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 6. PHASE 3: THE PAYMENT PLANS (NEW) ---
elif st.session_state.app_state == 'step_3_plans':
    st.markdown("<h1><span class='s-red'>S</span>isi <span class='s-green'>Sacco</span> Onboarding</h1>", unsafe_allow_html=True)
    st.progress(0.75, text=f"Step 3 of 4: Select Your Contribution Plan, {st.session_state.member_name}")
    
    st.markdown("### 💰 Choose Your Wealth Strategy")
    st.write("Sisi Sacco integrates with **M-Pesa Ratiba (2026)**. Your contributions will be automated securely.")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class='plan-card'>
            <h2 style='color: #64748b;'>🌱 The Hustler</h2>
            <h1 style='color: #0f172a;'>KES 100</h1><p>Per Day</p>
            <hr>
            <p>✓ Daily Auto-Deduction</p>
            <p>✓ Eligible for 3x Loans</p>
            <p>✓ Micro-Emergency Fund</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Select Hustler"): st.session_state.app_state = 'step_4_dashboard'; st.rerun()
            
    with c2:
        st.markdown("""<div class='plan-card' style='border-color: #10b981; box-shadow: 0 10px 20px rgba(16,185,129,0.1);'>
            <h2 style='color: #10b981;'>🌿 The Standard</h2>
            <h1 style='color: #0f172a;'>KES 5,000</h1><p>Per Month</p>
            <hr>
            <p>✓ Monthly Auto-Deduction</p>
            <p>✓ Eligible for 3x Loans</p>
            <p>✓ 3.5% Safaricom Yield</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Select Standard"): st.session_state.app_state = 'step_4_dashboard'; st.rerun()

    with c3:
        st.markdown("""<div class='plan-card'>
            <h2 style='color: #ef4444;'>🌳 The Sovereign</h2>
            <h1 style='color: #0f172a;'>KES 50,000</h1><p>Per Month</p>
            <hr>
            <p>✓ Elite Concierge Support</p>
            <p>✓ Massive Loan Limit</p>
            <p>✓ Business Investment Priority</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Select Sovereign"): st.session_state.app_state = 'step_4_dashboard'; st.rerun()

# --- 7. PHASE 4: THE MAIN DASHBOARD ---
elif st.session_state.app_state == 'step_4_dashboard':
    st.balloons()
    col_head, col_badge = st.columns([3, 1])
    with col_head:
        st.markdown("<h1><span style='color:#ef4444'>S</span>isi <span style='color:#10b981'>Sacco</span></h1>", unsafe_allow_html=True)
    with col_badge:
        st.markdown("<div style='text-align:right; margin-top:20px;'><span style='background:#dcfce7; color:#166534; padding:8px 16px; border-radius:30px; font-weight:bold; font-size:12px; border: 1px solid #166534;'>🛡️ y + 4/more ACTIVE</span></div>", unsafe_allow_html=True)

    st.success(f"Welcome to your Financial Fortress, {st.session_state.member_name}. Your M-Pesa Ratiba is locked in.")
    st.divider()

    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Group Savings (95%)", f"KES {st.session_state.sacco['total_vault']:,.0f}", "Fortress Mode")
    with m2: st.metric("Stability Vault (5%)", f"KES {st.session_state.sacco['stability_pool']:,.2f}", "Loan Source")
    with m3: st.metric("Yield Rate", "3.5%", "Daily Accrual")

    t1, t2, t3 = st
