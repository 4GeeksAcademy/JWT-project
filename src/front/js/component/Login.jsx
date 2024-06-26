import React, { useState, useContext } from 'react'
import { Context } from "../store/appContext";
import { useNavigate } from 'react-router-dom';

export const Login = () => {
    const [login, setLogin] = useState({
        "email":'',
        "password": ''
    })
    const {store, actions} = useContext(Context);
    const navigate = useNavigate();

    const handleChange =(e)=>{           
        setLogin({...login, [e.target.name]: e.target.value});
    };

    const handleLogin = async(e)=>{
        e.preventDefault();
        if(login.email && login.password){
            const resp = await actions.checkUserLogin(login);
            if(resp.success){
                navigate('/UserProfile')
            }else{
                alert(resp.error || 'login failed')
            } 
        }else{
            alert('Email and password are required')
        }
    }

    
    
    return (
        <div>
            <form className="d-flex" onSubmit={handleLogin}>
                <label htmlFor='username' className='form-label'>Email</label>
                <input name='email' id='username' className="form-control me-2" type="email" placeholder="example@email.com" vale='email' onChange={handleChange}/>

                <label htmlFor="password" className="form-label">Password</label>
                <input name='password' id="password" type="password" value={login.password} onChange={handleChange}></input>
                
                <button className="btn btn-outline-success" type="submit">Submit</button>
            </form>
        </div>
    )
}
