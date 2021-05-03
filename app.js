/* retrieve cupcake info from DB */

BASE_API_URL = "http://localhost:5000/api/cupcakes"

async function get_cupcake_info(evt){
    evt.preventDefault();

    let cupcakeFormData = 

    
    let response = await axios.get(BASE_API_URL);
    console.log(response);
} 

