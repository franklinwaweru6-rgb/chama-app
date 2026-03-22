import streamlit as st
import time

# --- 1. GLOBAL BRANDING & THEME ---
st.set_page_config(page_title="Sisi Sacco", page_icon="S", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    
    /* Cinematic Splash */
    .splash-container {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.95)), 
                    url('https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=1500&q=80');
        background-size: cover; z-index: 9999; display: flex; flex-direction: column; 
        align-items: center; justify-content: center; color: white; text-align: center;
    }
    .s-red { color: #ef4444; } .s-green { color: #10b981; }
    
    /* Progress Loader */
    .loader-bar { width: 300px; height: 6px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; margin-top: 20px;}
    .loader-progress { width: 0%; height: 100%; background: #10b981; animation: load 4s linear forwards; }
    @keyframes load { 0% { width: 0%; } 100% { width: 100%; } }

    /* Hierarchy & Cards */
    .inviter-card { background: #1e293b; color: white; border-radius: 20px; padding: 30px; border: 2px solid #ef4444; margin-bottom: 25px; }
    .governance-card { background: white; border-radius: 20px; padding: 25px; border-top: 5px solid #10b981; box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
    .stButton>button { width: 100%; border-radius: 50px; height: 3.5rem; background: #10b981; color: white !important; font-weight: 700; border: none; transition: 0.3s; }
    .stButton>button:hover { background: #ef4444; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# --- 2. SOVEREIGN STATE ROUTER ---
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'splash'
if 'hierarchy' not in st.session_state:
    st.session_state.hierarchy = {
        'inviter': None, 
        'overseer': None, 
        'chair': None, 
        'treasurer': None, 
        'secretary': None
    }

# --- 3. PHASE 0: THE CINEMATIC SPLASH (9s) ---
if st.session_state.app_state == 'splash':
    p = st.empty()
    with p.container():
        st.markdown('<div class="splash-container"><h1><span class="s-red">S</span>ISI <span class="s-green">SACCO</span></h1><p style="letter-spacing:5px;">THE INVITER PROTOCOL</p></div>', unsafe_allow_html=True)
        time.sleep(5)
    with p.container():
        st.markdown('<div class="splash-container"><h3>INITIALIZING SOVEREIGN SEED...</h3><div class="loader-bar"><div class="loader-progress"></div></div></div>', unsafe_allow_html=True)
        time.sleep(4)
    st.session_state.app_state = 'inviter_entry'
    st.rerun()

# --- 4. PHASE 1: THE INVITER (The Seed) ---
if st.session_state.app_state == 'inviter_entry':
    st.markdown("<div class='inviter-card'>", unsafe_allow_html=True)
    st.title("🛡️ The Inviter's Command")
    st.write("The Sacco journey begins with you. Enter your name to initiate the invitation protocol.")
    inv_name = st.text_input("Full Legal Name of Inviter:")
    if st.button("Initialize Sacco"):
        if inv_name:
            st.session_state.hierarchy['inviter'] = inv_name
            st.session_state.app_state = 'overseer_election'
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. PHASE 2: OVERSEER ELECTION (Foundation) ---
elif st.session_state.app_state == 'overseer_election':
    st.title("⚖️ Election Phase: The Overseer")
    st.write(f"**Invited by:** {st.session_state.hierarchy['inviter']}")
    st.info("The Overseer is the ultimate watchdog. They hold the power to audit all leaders.")
    o_name = st.text_input("Elect the Overseer:")
    if st.button("Confirm Overseer Election"):
        if o_name:
            st.session_state.hierarchy['overseer'] = o_name
            st.session_state.app_state = 'leader_nominations'
            st.rerun()

# --- 6. PHASE 3: RISING HIERARCHY (Nominations) ---
elif st.session_state.app_state == 'leader_nominations':
    st.title("⬆️ Rising Hierarchy: Nominate Leaders")
    st.write(f"**Overseer Active:** {st.session_state.hierarchy['overseer']}")
    
    col1, col2 = st.columns(2)
    with col1:
        c_name = st.text_input("Nominate Chair:")
        t_name = st.text_input("Nominate Treasurer:")
    with col2:
        s_name = st.text_input("Nominate Secretary:")
        st.write("---")
        st.caption("Note: These roles are overseen by the elected Overseer.")
        
    if st.button("Finalize Executive Board"):
        if c_name and t_name and s_name:
            st.session_state.hierarchy.update({'chair': c_name, 'treasurer': t_name, 'secretary': s_name})
            st.session_state.app_state = 'chair_strategy'
            st.rerun()

# --- 7. PHASE 4: THE CHAIR'S SELECTION (The Strategy) ---
elif st.session_state.app_state == 'chair_strategy':
    st.title(f"👑 Chair's Executive Choice: {st.session_state.hierarchy['chair']}")
    st.markdown(f"**Monitoring Overseer:** <span style='color:#ef4444'>{st.session_state.hierarchy['overseer']}</span>", unsafe_allow_html=True)
    
    st.markdown("<div class='governance-card'>", unsafe_allow_html=True)
    plan = st.radio("Primary Payment Cycle:", ["6-Month Growth Plan", "Yearly Sovereign Plan"])
    sub_plan = st.selectbox("Contribution Tier:", ["Bronze (Hustler)", "Silver (Standard)", "Gold (Elite)"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Confirm Strategy & Lock Plans"):
        st.session_state.selection = {"main": plan, "sub": sub_plan}
        st.session_state.app_state = 'treasurer_execution'
        st.rerun()

# --- 8. PHASE 5: THE TREASURER'S HANDSHAKE (The Payment) ---
elif st.session_state.app_state == 'treasurer_execution':
    st.title(f"💰 Treasurer Execution: {st.session_state.hierarchy['treasurer']}")
    st.write(f"Executing: **{st.session_state.selection['main']}** | Tier: **{st.session_state.selection['sub']}**")
    
    st.markdown(f"""
    <div style='background: #fee2e2; padding: 25px; border-radius: 15px; border: 2px solid #ef4444;'>
        <b>GOVERNANCE LOCK STATUS:</b><br>
        - CHAIR ({st.session_state.hierarchy['chair']}): PLAN APPROVED<br>
        - OVERSEER ({st.session_state.hierarchy['overseer']}): WATCHING TREASURY
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Trigger M-Pesa Ratiba Payment"):
        with st.spinner("Processing Sovereign Payment Handshake..."):
            time.sleep(3)
            st.session_state.app_state = 'final_dashboard'
            st.rerun()

# --- 9. PHASE 6: THE FINAL MASTER DASHBOARD ---
elif st.session_state.app_state == 'final_dashboard':
    st.balloons()
    col_l, col_r = st.columns([3, 1])
    with col_l:
        st.title("🏛️ Sisi Sacco Dashboard")
        st.write(f"Inviter: **{st.session_state.hierarchy['inviter']}** | Overseer: **{st.session_state.hierarchy['overseer']}**")
    with col_r:
        st.markdown("<br><span style='background:#dcfce7; color:#166534; padding:10px 20px; border-radius:30px; font-weight:bold; border: 1px solid #166534;'>🛡️ VAULT SECURED</span>", unsafe_allow_html=True)

    st.divider()
    
    # Financial Pillars
    m1, m2, m3 = st.columns(3)
    m1.metric("Active Strategy", st.session_state.selection['main'])
    m2.metric("Sub-Tier Plan", st.session_state.selection['sub'])
    m3.metric("Hierarchy Status", "y + 4 Verified")

    t1, t2 = st.tabs(["📊 Portfolio", "⚖️ Governance Audit"])
    
    with t1:
        st.markdown("<div class='governance-card'><h3>Vault Portfolio</h3><p>Strategy selected by Chair, executed by Treasurer, audited by Overseer.</p></div>", unsafe_allow_html=True)
        st.progress(0.05, text="Group Savings Accumulating...")
        
    with t2:
        st.subheader("Immutable Hierarchy")
        st.write(f"**Chair:** {st.session_state.hierarchy['chair']}")
        st.write(f"**Treasurer:** {st.session_state.hierarchy['treasurer']}")
        st.write(f"**Secretary:** {st.session_state.hierarchy['secretary']}")
        st.success("The 2/3 Member vote is active for all future oversight.")
