import './App.css';
// import About from './components/About';
import Navbar from './components/Navbar';
import TextForm from './components/TextForm';
import React, {useState} from 'react';

function App() {

  const [theme, setTheme] = useState('white');
  const toggleTheme=()=>{
    if (theme==='white')
    {
      setTheme('black');
      document.body.style.backgroundColor = '#01061c';
      document.body.style.color = 'white';
    }
    else
    {
      setTheme('white');
      document.body.style.backgroundColor = '#d7dfff';
      document.body.style.color = 'black';
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