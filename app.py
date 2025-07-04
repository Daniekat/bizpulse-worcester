
import streamlit as st

st.set_page_config(page_title="BizPulse Worcester", layout="centered")

st.title("📢 BizPulse Worcester")
st.markdown("""
Welkom by **BizPulse Worcester** – jou een-stop platform vir:
- 🛡️ Sekuriteitswaarskuwings
- 🌱 Goeie Nuus & Projekte
- 📅 Gemeenskapsgeleenthede
- ✉️ Kitsboodskappe aan ander besigheidseienaars

---

ℹ️ **Let wel:** Hierdie platform is ontwerp vir die sakegemeenskap van Worcester.  
""")

st.sidebar.title("Navigasie")
section = st.sidebar.radio("Gaan na:", ["Sekuriteit", "Goeie Nuus", "Kalender", "Kontak"])

if section == "Sekuriteit":
    st.subheader("🛡️ Sekuriteitswaarskuwings")
    st.info("Geen nuwe waarskuwings op hierdie oomblik.")

elif section == "Goeie Nuus":
    st.subheader("🌱 Goeie Nuus")
    st.success("WCID het 20 nuwe bome geplant in die middedorp!")

elif section == "Kalender":
    st.subheader("📅 Gebeure & Kalender")
    st.warning("Maandag: Besigheidseienaars vergadering om 17:30 by Die Kelder.")

elif section == "Kontak":
    st.subheader("✉️ Kontak / Stuur Waarskuwing")
    st.text_input("Tik jou boodskap hier...")
    st.button("Stuur")

st.markdown("---")
st.caption("Powered by D. Rousseau")
