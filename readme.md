# flask boilerplate with user-system ${{\color{Goldenrod}\small{ \texttt{ WIP \}}}}\$
minimal flask boilerplate for security/user/login with factory pattern, browser-sync, flowbite/tailwind (dark-/light-theme).

## install 
- `python -m venv venv` & `venv\Scripts\activate`
- `npm i`
- `pip install -r requirements.txt` 
- adjust `config.py` if needed (e.g. database swap)
- adjust `.env` if needed
- adjust `bs-config.py` if needed

## run/dev
- `npm run serverbs` to start browser-sync 
- `npx tailwindcss -i ./app/static/src/input.scss -o ./app/static/dist/css/output.css --watch` to start css watch
- `python run.py` to run app 
- one-time/optional: `python setup.py` to create db
- check sqlite db: `sqlite3 instance/boilerplate.db` => `select * from user; `, `.tables`, `.databases`, `.show`

## content
- `/index`, `/` as default home route 
- `/login` provided by flask-security-too
- `/register` provided by flask-security-too
- custom `/security` templates for `login_user.html` and `register_user.html`
- default example models/db-structure for `user`, `role` and `roles_users`

## sqlite example data  


| id  | email      | username | password   | active | confirmed_at | current_login_at     | last_login_at        | current_login_ip | last_login_ip | login_count | fs_uniquifier_placeholder |
|-----|------------|----------|----------- | ------ |--------------|------------------    |--------------------  |------------------|---------------|-------------|-------------------------- |
| <id>   | <mail> |          | <hsahedpw> | 1      | 			   | 2024-06-22 21:47:58  | 2024-06-22 21:47:58  | 127.0.0.1 		|	 			| 1           | fs_uniquifier_placeholder |



## notes/hints
- factory pattern: `run.py` => `factory.py` => `routes`, `extensions`, `models`, `security`
```jsx
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
- ...git 