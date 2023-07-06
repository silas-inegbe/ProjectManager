import Header from "../Components/Header";
import Footer from "../Components/Footer";
import styled from "styled-components";
import Intro from "../Components/Intro";
import { Link } from "react-router-dom";
import { useState } from "react";
import React, { lazy, Suspense } from "react";


const Container = styled.div`
 position: relative;
  .sec1 {
    background-color: #f8f9fa;
    margin: 0;
    padding: 80px 0px 90px 0px;
    display: flex;
    flex-direction: column;
    position: relative;

    div.first {
      background-color: #ff8a00; //write a javascript function?
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #fff;
      height: 30vh;
      margin-top: 0px;
      padding-top: 0px;

      h3 {
        font-size: 50px;
        font-weight: 200;
        margin-top: -20px;
      }

      .dialogue {
        display: flex;
        align-items: center;
         /* justify-content: center;  */
        flex-direction: column;
        padding-top: 2%;
        border: 1px solid ;
        border-color: #F1F1F1;
        border-radius: 30px;
        height: 85vh;
        width: 75vh;
        top: 30vh;
        position: absolute;
        background-color: #fff;

        button{
          height: 60px;
          width: 90%;
          border-radius: 10px;
          border: 1px solid;
          border-color: #98A1AD;
          font-size: 18px;
          font-weight: 600;
          font-family: inherit;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 10px;

        }
        button:hover{
          cursor: pointer;
        }
        button.submit{
          background-color:#001935 ;
          width: 100%;
          font-size: 17px;
          margin-top: 03%;
          color: #fff;
          
        }
        button.submit:hover{
          cursor: pointer;
          background-color: #ff8a00;
          transition: ease-in-out 0.1s;
        }

        h4{
          color: #2F444E;
          display: flex;
          gap: 5px;
          align-items: center;
          hr{
            width: 215px;
            height: 0px;
          }
        }
      

        form {
           /* border: 1px solid red;  */
          padding: 0px;
          display: flex;
          flex-direction: column;
          gap: 30px;
          margin: 0px;
          padding-top: 10px; 
          align-items: center;
           /* justify-content: center;  */
          height: 70%;
          width: 95%;

          span{
             /* border: 1px solid black;  */
            width: inherit;
            display: flex;
            flex-direction: column;
            align-items: start;
            
            h4{
              margin: 5px;
              margin-left: 0px;
              font-size: 14px;
               /* position: relative;
              left: -35%;  */
            }
          }
          
          span.line{
            padding-left: 3%;

            p{
                margin: 0px;
                margin-left: 05px;
                font-size: 10px;
                color: red;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;

            }
            p.valid-email{
                color: green;
            }
          }
          span.submit{
            display: flex;
            flex-direction: column;
            align-items: baseline;
            justify-content: center;
            align-items: center;
            margin-top: 2%;
            gap: 5px;

            a{
              text-decoration: none;
              color: #ff8a00;
            }
            a:hover{
              color: #ff1a11;
            }
          
          }
          input {
            height: 40px;
            width: 95%;
            border-radius: 10px;
            overflow: hidden;
            outline: none;
            border: 1px solid #ff8a00;
            opacity: 80%;
            padding-left:10px ;
            font-family: inherit;
            font-size:1rem!important;

            }
          }
        }
      }
    }
  .sec2 {
    background-color: #f8f9fa;
    height: 60vh;
  }

`
// const LazyHeader = lazy(() => import("./Register"));
// const Test = () => {
//     return (
//       <div>
//         <Suspense fallback={<div>Loading...</div>}>
//           <LazyHeader />
//         </Suspense>
//       </div>
//     );
//   };



const Register = () => {
    const [email, setEmail] = useState('');
    const [isValid, setIsValid] = useState(false);
  
    const handleEmailChange = (e) => {
      const inputEmail = e.target.value;
      setEmail(inputEmail);
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      setIsValid(emailRegex.test(inputEmail));
    };
  
    return (
        <Container>
        <Header></Header>
        <section className="sec1">
          <Intro></Intro>
          <div className="first">
            <h3>
              <b>Create your account</b>
            </h3>
            <div className="dialogue">
              <form action="submit">
                <span className="line">
                  <h4>Name *</h4>
                  <label htmlFor="text"></label>
                  <input type="text" id="name" placeholder="Enter Name" required />
                </span>
  
                <span className="line">
                  <h4>Email *</h4>
                  <label htmlFor="email"></label>
                  <input
                    type="email"
                    id="email"
                    placeholder="Enter Email"
                    value={email}
                    onChange={handleEmailChange}
                    required
                    noValidate
                  />
                  {isValid ? (
                    <p className="valid-email">Valid email address!</p>
                  ) : (
                    <p className="invalid-email">Invalid email address!</p>
                  )}
                </span>
                  <span className="line">
                    <h4>Password  *</h4>
                    <label htmlFor="pass"></label>
                    <input type="password" id="pass" placeholder="Enter Password" required/>
                  </span>

                <span className="line">
                    <h4>Company Name  *</h4>
                    <label htmlFor="email"></label>
                    <input type="text" id="email" placeholder="Enter Company" required/>   
                  </span>
                <span className="submit">
                  <button className="submit">Submit</button>
  
                 <h4>Already Have an Account? <Link to="/login">
                 <b>Sign In</b>
                 </Link>  </h4>
                </span>
                
              </form>
            </div>
          </div>
        </section>
        <section className="sec2"></section>
  
        <Footer></Footer>
      </Container>
     );
}
 
export default Register;