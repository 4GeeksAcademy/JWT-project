import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export const PrivateRoute = ({children}) => {
    const navigate = useNavigate()
    const token = localStorage.getItem('jwt-token')

    useEffect(()=>{
        if(!token){
            navigate('/')
        }
    },[token, navigate])

  return token ? children : null 
  
}
