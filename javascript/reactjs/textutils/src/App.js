import './App.css';
// import About from './components/About';
import Navbar from './components/Navbar';
import TextForm from './components/TextForm';
import React, {useState} from 'react';

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
  const toggleTheme=()=>{
    if (theme.mode==='light')
    {
      setTheme(darkTheme);
      document.body.style.backgroundColor = darkTheme.backgroundColor;
      document.body.style.color = darkTheme.fontColor;
      
    }
    else
    {
      setTheme(lightTheme);
      document.body.style.backgroundColor = lightTheme.backgroundColor;
      document.body.style.color = lightTheme.fontColor;
    }
  }

  return (
    <>
      <Navbar title="TextUtils" theme={theme} toggleTheme={toggleTheme}/>
      <div className='container my-3'>
        <TextForm heading='Enter the Text to Analyze' theme={theme}/>
        {/* <About></About> */}
      </div>
    </>
  );
}

export default App;