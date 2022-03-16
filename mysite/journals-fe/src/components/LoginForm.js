import React, { useCallback } from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import { GoogleLogin } from 'react-google-login';
import axios from "axios";
import { API_URL } from "../constants";

const onGoogleLoginSuccess = useCallback(
  response => {
    const idToken = response.tokenId;
    const data = {
      email: response.profileObj.email,
      first_name: response.profileObj.givenName,
      last_name: response.profileObj.familyName
    };

    validateTokenAndObtainSession({ data, idToken })
      .then(handleUserInit)
      .catch(notifyError);
  },
  [handleUserInit]
);


const Login = () => {
  return (
    <GoogleLogin
      clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}  // your Google app client ID
      buttonText="Sign in with Google"
      onSuccess={onGoogleLoginSuccess} // perform your user logic here
      onFailure={onGoogleLoginFailure} // handle errors here
    />
  );
};

export const validateTokenAndObtainSession = ({ data, idToken }) => {
  const headers = {
    Authorization: idToken,
    'Content-Type': 'application/json'
  };

  return axios.post('users/init/', data, { headers });
};