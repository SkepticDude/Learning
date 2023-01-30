import './App.css';
// import About from './components/About';
import Navbar from './components/Navbar';
import TextForm from './components/TextForm';
import React, {useState} from 'react';
import Alert from './components/Alert';

function App() {

  let darkTheme = {
    mode : 'dark',
    backgroundColor : '#07101B',
    fontColor: 'white'
  }
  let lightTheme = {
    mode : 'light',
    backgroundColor : 'white',
    fontColor : 'black'
  }
  
  const [theme, setTheme] = useState(lightTheme);
  const [alert, setAlert] = useState(null);

  const showAlert = (type, message) =>
  {
    setAlert(
      {
        type : type,
        msg : message
      }
    )
    setTimeout(() => {
      setAlert(null);
    }, 2000);
  }

  const toggleTheme=()=>{
    if (theme.mode==='light')
    {
      setTheme(darkTheme);
      document.body.style.backgroundColor = darkTheme.backgroundColor;
      document.body.style.color = darkTheme.fontColor;
      showAlert("success","Dark theme has been enabled");
      
    }
    else
    {
      setTheme(lightTheme);
      document.body.style.backgroundColor = lightTheme.backgroundColor;
      document.body.style.color = lightTheme.fontColor;
      showAlert("warning","Light theme has been enabled");
    }
  }

  return (
    <>
      <Navbar title="TextUtils" theme={theme} toggleTheme={toggleTheme}/>
      <Alert alert={alert}/>
      <div className='container my-3'>
        <TextForm showAlert={showAlert} heading='Enter the Text to Analyze' theme={theme}/>
        {/* <About></About> */}
      </div>
    </>
  );
}

export default App;