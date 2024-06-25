const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			currentRole: "",

		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			// getMessage: async () => {
			// 	try {
			// 		// fetching data from the backend
			// 		const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
			// 		const data = await resp.json()
			// 		setStore({ message: data.message })
			// 		// don't forget to return something, that is how the async resolves
			// 		return data;
			// 	} catch (error) {
			// 		console.log("Error loading message from backend", error)
			// 	}
			// },
			checkUserLogin: async(login)=>{
				try{
					const response = await fetch(`${process.env.BACKEND_URL}/api/user/login`,{
						method: 'POST',
						header: {'Content-Type': 'application/json'},
						body: JSON.stringify(login)
					});
					const data = await response.json()
					if (response.ok){
						console.log('user logged')
						return {success: true}
					}else{
						console.log('Error loging')
						return {success: false, error: data.error}
					}
				}
				catch(e){
					console.error(e)
				}
			},
			checkUserSesion: async (signup) => {
				// const store = setStore()
				console.log("funciona", signup)
				try {
					// error en el fetch
					const response = await fetch(`${process.env.BACKEND_URL}/api/user/signup`, {
						method: 'POST',
						header: { 'Content-Type': 'application/json' },
						body: JSON.stringify(signup)
					});
					const data = await response.json()
					if (response.ok) {
						console.log("usuario creado", data)
						return { success: true }
					} else {
						console.log("Data not send")
						return { success: false, error: data.error }
					}
				}
				catch (e) {
					console.error(e)
				}
			}
		}
	};
};

export default getState;
