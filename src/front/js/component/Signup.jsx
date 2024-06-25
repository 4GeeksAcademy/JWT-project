import React, {useState, useContext} from 'react'
import { Context } from '../store/appContext'

export const Signup = () => {
    const {store,actions} = useContext(Context)
    const [signup, setSignup] = useState({
        "email":'',
        "password": '',
        "phone_number":''
    })

    const info =(e)=>{
        setSignup({...signup, [e.target.name]: e.target.value})
    }
    
    const submit =(e)=>{
        e.preventDefault()
        actions.checkUserSesion(signup)
    }
    return (
        <div>
            <form className="d-flex">
                <label htmlFor='username' className='form-label'>Email</label>
                <input id='username' className="form-control me-2" type="email" placeholder="example@email.com" onChange={info} name="email" value={signup.email}/>

                <label htmlFor="password" className="form-label">Password</label>
                <input id="password" type="password" onChange={info} name="password" value={signup.password}></input>

                <label htmlFor="phone" className="form-label">Phone</label>
                <input id="phone" type="number" onChange={info} name="phone_number" value={signup.phone_number}></input>

                <button className="btn btn-outline-success" type="submit" onClick={submit}>Submit</button>
            </form>
        </div>
    )
}
