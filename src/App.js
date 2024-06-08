import logoOf from './img/logo.svg';
import './App.css';
import React from "react";
import axios from "axios";

function App() {
  const [text, setText] = React.useState("");
  const [resText, setResText] = React.useState("");

  function clearData (){
    setResText("Waiting for input...")
  };

  function handleChange(e) {
    const value = e.target.value;
    setText(value);
  };

  function handleSubmit() {
    let data = JSON.stringify({
      "message": text
    });
    
    let config = {
      method: 'post',
      maxBodyLength: Infinity,
      url: 'http://127.0.0.1:5000/api/post_example',
      headers: { 
        'Content-Type': 'application/json'
      },
      data : data
    };
    
    axios.request(config)
    .then((response) => {
      console.log("ApiRes: " , response?.data)
      setResText(response?.data?.message);
    })
    .catch((error) => {
      console.log(error);
    });
  }

  return (
    <div className="">
      <div className="App">
        <header className="App-header">
          <img src={logoOf} className="App-logo" alt="logo" />
          <p>Hate Speech Detection Model</p>
          <a className="App-link" href="#Screen1" rel="noopener noreferrer">
            Explore
          </a>
        </header>
      </div>

      <div className="container mrtop">
        <div class="mb-3" id="Screen1">
          <label for="exampleFormControlTextarea1" class="form-label left">
            Text area
          </label>
          <textarea
            class="form-control txhight"
            id="exampleFormControlTextarea1"
            rows="3"
            onClick={clearData}
            onChange={handleChange} placeholder='Enter your text here!'>{text}
          </textarea>          
          <button type="button" class="btn btn-success mrtop" onClick={handleSubmit}>Submit</button>
          <p>{`${resText}`}</p>
        </div>
      </div>

      
      <div class="card text-center">
        <div class="card-body">
          <p class="card-text">All © Copyrights reserve to Vikash Sharma and teams.</p>
        </div>
      </div>
    </div>
  );
}

export default App;