
const Note=({deleteData,readNote,title,date,data_id})=>{
  const getDate=(date)=>{
      return new Date(date).toLocaleDateString();
   }

  return(
    <div onClick={()=>readNote(data_id)} className="bg-gray-800 p-4 rounded hover:border-l-4 border-indigo-400 flex justify-between items-center">
      <div>
        <h1 className="font-bold text-white">{title}</h1>
        <h3 className="font-bold text-white">{getDate(date)}</h3>
      </div>
    </div>
  )
}

export default Note
