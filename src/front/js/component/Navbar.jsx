import React from 'react'
import { useNavigate } from 'react-router-dom'

export const Navbar = () => {
    const navigate = useNavigate()
    const handleSingOut =(e)=>{
        localStorage.removeItem('jwt-token')
        navigate('/')
    }
    return (
        <nav className="navbar navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand">Navbar</a>
                <button onClick={handleSingOut}>signOut</button>
            </div>
        </nav>
    )
}

