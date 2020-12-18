import React, {useState} from 'react'
import Base from '../core/Base';
import {Link} from 'react-router-dom';
import {signup} from '../auth/helper.js/index';

const Signup = () => {

    const [values, setValues] = useState({
        name:"",
        email:"",
        password:"",
        error:"",
        success:false,
    });

    const {name, email, password, error, success} =values;

    const handleChange =(name) => (event) => {
        setValues({ ...values, error:false, [name]:event.target.value});
    }

    // const signUpForm = ()=>{
    //     return(
    //         d
    //     )
    // }

    return (
        <Base title ="sign up page" description ="A signup for ck_site user">
            <p>sign up page</p>
        </Base>
    );
}
;
export default Signup;