import {BrowserRouter as Router,Routes,Route} from "react-router-dom";
import {useState,useEffect} from "react";
import Navbar from "./components/Navbar";

import Home from "./Home";
import About from "./views/About";
import EditNote from "./views/EditNote";
import AddNote from "./views/AddNote";

function App() {
  const [notes,setNotes]=useState([]);
  let CSRF=document.cookie.slice(10);
//  let apiHost="localhost:8000";

  useEffect(()=>{
     const fetchNotes=async()=>{
        const res=await fetch(`/api/notes/`);
        const data=await res.json();
       setNotes(data);
     }

     fetchNotes();
  },[]);


  const getDate=()=>{
     let d=new Date();
     let months=["Jan","Feb","Mar","Apri","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"];
     let days=["Sun","Mon","Tue","Wed","Thur","Fri","Sat"];
  
     let day=days[d.getDay()];
     let date=d.getDate();
     let month=months[d.getMonth()];
     let year=d.getFullYear();
     return `${day} ${date} ${month},${year}`;
   }

  const saveData=async (e,Title,Body)=>{
   e.preventDefault();
   const note={
    title:Title,
    body:Body
   }

   await fetch(`/api/notes/addnote`,{
     method:"POST",
     headers:{
      "Content-type":"application/json",
      "X-CSRFToken":CSRF
     },
     body:JSON.stringify(note)
   });
   window.location.replace("/");
  }


 const getNote=async (id)=>{
   const res=await fetch(`/api/notes/${id}/`,{
      method:"GET"
    });
    const data=await res.json();
    return data;
 }

 
 const editData=async (e,title,body,id)=>{
   e.preventDefault();
   let newData={title,body};
//   let CSRF=document.cookie.slice(10);

   await fetch(`/api/notes/${id}/update/`,{
     method:"PUT",
     headers:{
      "Content-Type":"application/json",
      "X-CSRFToken":CSRF
     },
     body:JSON.stringify(newData)
   });
  
   window.location.replace("/");
  }

  const deleteData=async(data_id,redirect)=>{
   await fetch(`/api/notes/${data_id}/delete/`,{
     method:"DELETE",
     headers:{
      "Content-Type":"application/json",
      "X-CSRFToken":CSRF
     }
   });
   const newNotes=notes.filter((note)=>(data_id !== note.id));
   setNotes(newNotes);
   if(redirect){
     window.location.replace("/");
   }
  }

  return (
    <Router>
       <div className="ease-in duration-200 w-screen h-screen bg-slate-900 pt-4">
         <Navbar />
          <Routes>
              <Route path="/" element={<Home notes={notes} deleteData={deleteData}/>}/>
           </Routes>
          <Routes>
             <Route path="about/" element={<About />}/>
          </Routes>
          <Routes>
            <Route path="editnote/:id/view/" element={<EditNote editData={editData} deleteData={deleteData} notes={notes}/>}/>
          </Routes>
          <Routes>
            <Route path="addnote/" element={<AddNote saveData={saveData}/>}/>
          </Routes>
        </div>
    </Router>
  );
}

export default App;
