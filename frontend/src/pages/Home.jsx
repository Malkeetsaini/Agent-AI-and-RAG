import {
  useEffect,
  useState
} from "react";

import {
  getProducts,
  searchProducts
} from "../api/productApi";

import CartDrawer from
"../components/CartDrawer";

import Navbar from
"../components/Navbar";

import ChatWidget
from "../components/ChatWidget";

import ProductCard from
"../components/ProductCard";

import SearchBar from
"../components/SearchBar";

export default function Home() {

  const [products, setProducts] =
    useState([]);

  useEffect(() => {

    loadProducts();

  }, []);

  const loadProducts = async () => {

    const data =
      await getProducts();

    setProducts(data);

  };

  const handleSearch =
    async (query) => {

      const results =
        await searchProducts(
          query
        );

      setProducts(results);

    };

  return (

    <div>

      <Navbar />

      {/*<CartDrawer />*/}

      <SearchBar
        onSearch={
          handleSearch
        }
      />

      <ChatWidget />

      {products.map((p) => (

        <ProductCard
          key={p.id}
          product={p}
        />

      ))}

    </div>

  );
}