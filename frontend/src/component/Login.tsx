import React, { useState } from "react";
import { fetchPost } from "../utils/request";
import { toast } from "react-toastify";

type Props = {
  setAuthenticated: (auth: boolean) => void;
  setToken: (token: string) => void;
  setUser: ({}) => void;
};

function Login({ setAuthenticated, setToken, setUser }: Props) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [fullname, setFullname] = useState("");
  const [isSignUp, setIsSignUp] = useState(false);

  // Función que maneja el registro de un nuevo usuario
  const signUp = async (event: React.FormEvent) => {
    event.preventDefault();
    const request = { username, password, fullname };
    const url = "http://localhost:5000/auth/signup";

    try {
      const response = await fetchPost(url, request);
      if (response.data.success) {
        setPassword("");
        setIsSignUp(false);
        toast.success("Registrado");
      } else {
        toast.error("Error en el registro:");
      }
    } catch (error) {
      toast.error("Error en el registro");
    }
  };

  // Función que maneja el inicio de sesión de un usuario
  const signIn = async (event: React.FormEvent) => {
    event.preventDefault();
    const request = { username, password };
    const url = "http://localhost:5000/auth/login";

    try {
      const response = await fetchPost(url, request);

      if (response.data.success) {
        setUser({ username, password });
        setAuthenticated(true);
        setToken(response.data.token);
      } else {
        toast.error("Error en el inicio de sesión:");
      }
    } catch (error) {
      toast.error("Error en el inicio de sesión:");
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div className="mb-3 row w-25">
        <h1>{isSignUp ? "Sign Up" : "Sign In"}</h1>
        <form
          onSubmit={isSignUp ? signUp : signIn}
          className="p-4 border rounded shadow bg-white"
        >
          <div className="mb-3">
            <label htmlFor="username" className="form-label">
              User:
            </label>
            <input
              id="username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="form-control"
              required
            />
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label">
              Password:
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="form-control"
              required
            />
          </div>
          {isSignUp && (
            <div className="mb-3">
              <label htmlFor="fullname" className="form-label">
                Fullname:
              </label>
              <input
                id="fullname"
                type="text"
                value={fullname}
                onChange={(e) => setFullname(e.target.value)}
                className="form-control"
                required
              />
            </div>
          )}
          <button type="submit" className="btn btn-primary w-100">
            {isSignUp ? "Sign Up" : "Sign In"}
          </button>
        </form>
        <button
          className="btn btn-secondary w-100 mt-2"
          onClick={() => setIsSignUp(!isSignUp)}
        >
          {isSignUp ? "Sign In" : "Sign Up"}
        </button>
      </div>
    </div>
  );
}

export default Login;
