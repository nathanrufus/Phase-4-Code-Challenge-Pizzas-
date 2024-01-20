import React from 'react'

function Navbar() {
  return (
    <div>
<header>
      <div className="logo">
        <img src={logo} alt="Pizza logo" />
        <h1>The Pizza Society</h1>
      </div>
      <nav>
        <Link to="/">Home</Link>
      </nav>
    </header>
    </div>
  )
}

export default Navbar