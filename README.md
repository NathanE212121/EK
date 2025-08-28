# index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EK Guest House - A Relaxing Stay in Chelenko</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
        }
        header {
            background-color: #004d40;
            color: #fff;
            padding: 1rem 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .logo img {
            height: 50px;
        }
        nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
        }
        nav ul li {
            margin: 0 15px;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease;
        }
        nav a:hover {
            color: #a5d6a7;
        }
        .hero-section {
            background: #e0f2f1;
            padding: 80px 20px;
            text-align: center;
        }
        .hero-section h1 {
            font-size: 3.5em;
            color: #004d40;
        }
        .hero-section p {
            font-size: 1.5em;
            color: #555;
        }
        .photo-gallery {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            padding: 40px;
            max-width: 1200px;
            margin: auto;
        }
        .photo-gallery img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            grid-column: span 1; /* Default for all images */
        }
        .photo-gallery .wide-image {
            grid-column: span 2; /* This image will span two columns */
        }
        .content-section {
            padding: 60px 20px;
            max-width: 1100px;
            margin: auto;
            text-align: center;
        }
        .content-section h2 {
            color: #004d40;
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        footer {
            background-color: #222;
            color: #eee;
            text-align: center;
            padding: 2rem 0;
            margin-top: 50px;
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">
            <img src="0.jpg" alt="EK Guest House Logo">
        </div>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="rooms.html">Rooms</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="booking.html">Book Now</a></li>
                <li><a href="https://maps.app.goo.gl/HMy6XD2g1J5Yy44i8">Map</a></li>  
            </ul>
        </nav>
    </header>

    <main>
        <section class="hero-section">
            <h1>Welcome to EK Guest House</h1>
            <p>Your Peaceful Retreat in Chelenko, Oromia</p>
        </section>

        <section class="photo-gallery">
            <img src="3.jpg" class="wide-image" alt="Promotional Banner of EK Guest House">
            <img src="1.jpg" alt="Street View of EK Guest House">
            <img src="2.jpg" alt="EK Guest House Exterior Building View">
        </section>
    </main>

    <footer>
        <p>© 2025 EK Guest House. All Rights Reserved.</p>
    </footer>

</body>
</html>
