import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['789012']).generate()

print(hashed_passwords)