# flask boilerplate with user-system ${{\color{Goldenrod}\small{ \texttt{ WIP \}}}}\$
minimal flask boilerplate for security/user/login with factory pattern, browser-sync, flowbite/tailwind (dark-/light-theme).

## install 
- req.: mysql db
- `npm i`
- `pip install -r requirements.txt`
- adjust `config.py` if needed
- adjust `.env` if needed
- adjust `bs-config.py` if needed

## run/dev
- `npm run serverbs` to start browser-sync 
- `npx tailwindcss -i ./app/static/src/input.scss -o ./app/static/dist/css/output.css --watch` to start css watch
- `python run.py` to run app 

## content
- `/index`, `/` as default home route 
- `/login` provided by flask-security-too
- `/register` provided by flask-security-too
- custom `/security` templates for `login_user.html` and `register_user.html`
- default example models/db-structure for `user`, `role` and `roles_users`

## notes/hints
- factory pattern: `run.py` => `factory.py` => `routes`, `extensions`, `models`, `security`
```bash
└───Flask Boilerplate
│ run.py
│
└───application
	│ factory.py
	│
├───static
	│ main.css
	│
├───templates
	│ register.html
	│
```

- flask-security-too =>
- npm 
	- flowbite, theme-mode, tailwind css
	- browser-sync, bs-config.js
- adjust/rename .env.example

## run/prod
- ...