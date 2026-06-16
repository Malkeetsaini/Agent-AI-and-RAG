export default function CartDrawer({

 cart

}){

 return (

  <div>

   <h3>
    Cart
   </h3>

   {
    cart.map(item=>(

     <div
      key={item.id}
     >

      {item.title}

     </div>

    ))
   }

  </div>

 );
}