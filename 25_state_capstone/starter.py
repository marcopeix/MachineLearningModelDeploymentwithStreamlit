import streamlit as st
import numpy as np
from joblib import load

# Initialize the session state with an empty prediction

# Function to load the model (use caching)

# Callback function to make a prediction.
# It updates the value of the prediction store in the state

if __name__ == "__main__":
    st.title("🍁Used car price calculator")

    # Load model

    with st.form(key="form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.number_input("Miles", value=9966.0, min_value=0.0, step=0.1, key="miles")
            st.selectbox("Model", index=0, key="model", options=['NSX', 'Avenger', '200', 'Ram 1500 Pickup', 'Explorer', 'F-150',
        'Ranger', 'Camaro', 'Volt', 'Corvette', 'LaCrosse', 'ELR',
        'Express Passenger', 'Silverado 2500HD', 'Silverado 3500HD',
        'Silverado 3500', 'Express Cargo', 'Sierra 3500 Chassis Cab',
        'Yukon', 'Yukon XL', 'Escalade', 'Challenger', 'Silverado 1500',
        'Silverado 1500 LD', 'Terrain', 'RX Hybrid', 'RX', 'Routan',
        'Ram 2500 Pickup', 'Fiesta', 'HHR', 'Sierra 1500',
        'Sierra 1500 Denali', 'Escalade EXT', '3 Series', 'Jetta', 'GLE',
        'GLE-Class', 'GLS', 'GL-Class', 'GLS-Class', 'H2', 'Aviator', 'X5',
        'X3', 'S60', 'RLX', 'Q50', 'M', 'Prius', 'Highlander', 'GS', 'LS',
        'CT6', 'S90', 'XC60', 'Discovery Sport', 'Defender', 'Range Rover',
        'Range Rover Sport', 'CLS-Class', 'AMGA GT 4-Door Coupe',
        'E-Class', 'Q5', 'allroad', 'A4', 'A5 Coupe', 'A5',
        'A3 Sportback e-tron', '5 Series', '7 Series', 'i3', 'I8', 'i8',
        'I3', 'C-Class', 'S-Class', 'Countryman', 'Panamera', 'Cayenne',
        'Touareg', 'XC90', 'GranTurismo', 'Hummer', 'Wrangler Unlimited',
        'All-New Wrangler Unlimited', 'Grand Cherokee', 'Gladiator',
        'Ram 1500 Classic', 'Ram Pickup', 'Transit', 'Transit Wagon',
        'Transit Passenger Van', 'F-550 Super Duty Chassis Cab',
        'F-450 Super Duty Chassis Cab', 'Transit Cutaway',
        'F-350 Super Duty Chassis Cab', 'F-250 Super Duty',
        'F-350 Super Duty', 'F-450 Super Duty', 'Transit Van',
        'E-Series Econoline Van', 'Econoline Van', 'F-350', 'Cruze',
        'Express Cutaway', 'Silverado 3500 Chassis Cab', 'Silverado',
        'Silverado Classic 2500HD', 'Colorado', 'Savana Cutaway',
        'Sierra 2500HD', 'Sierra 2500 Denali HD', 'Sierra 3500',
        'Sierra 3500HD', 'Sierra 3500 Denali HD', 'Sierra Classic 2500HD',
        'Sierra', 'Canyon', 'Liberty', 'Titan XD', 'Passat',
        'Ram 3500 Pickup', 'ProMaster Cargo Van', 'Ram 4500 Chassis Cab',
        'Ram 5500 Chassis Cab', 'Ram 3500 Chassis Cab', 'Equinox', 'CX-30',
        'Golf', 'Golf SportWagen', 'Beetle', 'Jetta SportWagen', 'M-Class',
        'R-Class', 'CX-5', 'F-Pace', 'F-PACE', 'XE', 'XF', 'Discovery',
        'Range Rover Velar', 'Sprinter Cab Chassis', 'Sprinter Van',
        'Sprinter Cargo Van', 'Q7', 'A7', 'A3', 'A6', 'GLK-Class',
        'Touareg 2', 'Civic', 'Aspen', 'Caliber', 'Caravan', 'Durango',
        'Dakota', 'Sebring', 'Cirrus', 'Dart', 'All-New Wrangler',
        'Wrangler', 'Wrangler JK', 'Wrangler JK Unlimited', 'Compass',
        'Patriot', 'Cherokee', 'Grand Caravan', 'Nitro', 'Expedition',
        'Fusion', 'Mustang', 'Focus', 'Five Hundred', 'Taurus',
        'Econoline Wagon', 'Club Wagon', 'E-Series Cutaway', 'Escape',
        'Freestyle', 'Taurus X', 'Explorer Sport Trac',
        'E-Series Econoline Wagon', 'Impala', 'Malibu Limited', 'Malibu',
        'Cobalt', 'Cavalier', 'Sonic', 'Cruze Limited', 'G5', 'Sunfire',
        'Solstice', 'Grand Am', 'Grand Prix', 'G6', 'Lucerne', 'LeSabre',
        'Verano', 'ATS', 'ATS Coupe', 'ATS Sedan', 'CTS Sedan',
        'CTS Sport Sedan', 'Catera', 'CTS', 'CTS Coupe', 'STS', 'CT4',
        'CT5', 'DeVille', 'ION', 'S-Series', 'L-Series', 'Sky', 'Aura',
        'Express', 'Astro', 'SSR', 'Silverado 1500HD', 'Savana', 'Envoy',
        'Acadia', 'Envoy XL', 'Montana', 'TrailBlazer', 'Blazer',
        'Uplander', 'Venture', 'Tahoe', 'Traverse', 'Suburban',
        'Savana Cargo', 'Sierra 1500HD', 'SRX', 'XT5', 'XT6', 'Accord',
        'Commander', 'Town Car', 'Continental', 'MKS', 'Altima',
        'Altima Sedan', 'Altima Coupe', 'Maxima', 'Titan', 'Frontier',
        'NV Cargo', 'Corolla', 'Prowler', 'Atlas Cross Sport', 'Atlas',
        'Mazda6', 'MAZDA6', 'Town & Country', 'Pacifica', 'Charger', '300',
        'Torrent', 'Magnum', 'Windstar', 'Edge', 'Flex', 'Monte Carlo',
        'Firebird', 'Regal', 'Century', 'XTS', 'Silverado Classic 1500',
        'Sierra 1500 Limited', 'Ridgeline', 'Odyssey', 'CR-V', 'Pilot',
        'Nautilus', 'MKX', 'MKT', 'Grand Marquis', 'XL7', 'Camry Solara',
        'Matrix', 'RAV4', 'Rav4', 'PT Cruiser', 'All-New Compass',
        'Journey', 'HR-V', 'Bronco Sport', 'Aveo5', 'Rendezvous', 'Trax',
        'Avalanche', 'VUE', 'Fit', 'Rio', 'RIO', 'Rio 5-Door', 'Accent',
        'Spectra', 'FORTE', 'Forte', 'Sephia', 'Forte5', 'MKZ', 'Yaris',
        'iA', 'Yaris iA', 'Mazda3', 'MAZDA3', 'Sentra', 'Versa',
        'Versa Sedan', 'Versa Note', 'Kicks', 'City Express', 'NV200',
        'Tacoma', 'Tiguan', 'Rabbit', 'New Jetta', 'Golf GTI', 'GTI',
        'New Beetle', 'Cabrio', 'Golf Alltrack', 'Eclipse',
        'Eclipse Spyder', 'Tribute', 'B-Series', 'Mariner', 'Legacy',
        'Impreza', 'Outback', 'Ascent', 'Tribeca', 'B9 Tribeca', 'Camry',
        'Avalon', 'Venza', 'Sienna', 'ES', 'NV Passenger', 'Passport',
        'Enclave', 'H3', 'Outlook', 'Accord Crosstour', 'Crosstour',
        'Element', 'MKC', 'Corsair', 'Navigator', 'Armada', 'Xterra',
        'Pathfinder', 'Rogue', 'Murano', 'Quest', 'Santa Fe',
        'Santa Fe Sport', 'Elantra', 'Sonata', 'Tundra', 'Sequoia', 'X4',
        'Optima', 'K5', 'New Optima', 'Sorento', 'Telluride', 'Vibe',
        'Corolla Hatchback', 'G8', 'Lancer', 'Outlander', 'Eclipse Cross',
        '124 Spider', 'Forester', 'XV Crosstrek', 'Crosstrek', 'Integra',
        'Protege5', 'Protege', 'MAZDA5', 'Mazda2', 'CX-3', 'MX-5 Miata',
        'CX-7', 'CX-9', 'Rogue Sport', 'cube', 'FX35', 'FX', 'QX70',
        'Kizashi', 'SX4 Crossover', 'SX4 Sedan', 'Grand Vitara', '4Runner',
        'Echo', 'Tercel', 'MR2 Spyder', 'FJ Cruiser', 'tC', 'xD', 'xB',
        'iQ', 'Corolla iM', 'iM', 'C-HR', 'Aveo', 'Encore', 'Trailblazer',
        'Spark', 'Tucson', 'Kona', 'Veracruz', 'Palisade', 'Elantra GT',
        'Elantra Touring', 'Elantra Coupe', 'Genesis', 'G80', 'Tiburon',
        'Genesis Coupe', 'Venue', 'Veloster', 'Rondo', 'Forte Koup',
        'Cadenza', 'Seltos', 'Soul', 'Sportage', 'Sedona', 'Carnival',
        'Entourage', 'Envision', 'Ecosport', 'EcoSport', 'Mirage',
        'Mirage G4', 'Transit Connect', 'E-PACE', 'E-Pace', 'Freelander',
        'Range Rover Evoque', 'Civic Hatchback', 'TT', 'Regal Sportback',
        'Regal TourX', 'Cascada', 'Astra', 'C-Class Cabriolet', 'Q3',
        'A6 Allroad', '8 Series', 'GLC Coupe', 'C-Class Coupe', '9-3',
        'S80', 'XC70', 'Renegade', 'Ghibli', '500X', 'Promaster City',
        'F12berlinetta', '458 Italia', '488 GTB', 'F8', 'Savana Passenger',
        'Escalade ESV', 'Ram Cargo Van', 'Captiva Sport', 'ILX', 'TL',
        'TLX', 'CL', 'Viper', 'Crossfire', 'Thunderbird', 'CTS-V Sedan',
        'ATS-V Sedan', 'DTS', 'XLR', 'XT4', 'ZDX', 'MDX', '500', '500c',
        'Ram SRT-10', 'QX50', 'EX', 'QX55', 'Endeavor', 'GLE-Class Coupe',
        'Z3', 'Z4', 'C-Class Sedan', 'RDX', 'JX', 'QX60', 'QX56', 'QX',
        'X7', 'X6', 'X5 M', 'X3 M', 'X4 M', 'WRX', 'WRX STI', 'BRZ',
        'FR-S', '86', 'TSX', 'Legend', 'RL', 'S2000', 'Miata',
        'MX-5 Miata RF', 'GT-R', 'Q70L', '350Z', '370Z', '350Z Roadster',
        '370Z Coupe', '370Z Roadster', 'G35', 'Q70', 'G Sedan', 'G Coupe',
        'G35 Sport Coupe', 'G', 'Q60 Coupe', 'G Convertible', 'JUKE',
        'Juke', 'Murano CrossCabriolet', 'QX80', 'Q45', 'G35 Coupe', 'IS',
        'LC', 'SC', 'RC', 'UX', 'NX', 'GX', 'LX', 'G90', 'Equus', 'G70',
        'GV80', 'Stinger', 'F-TYPE', 'F-Type', 'S-Type', 'XJ Series',
        'X-Type', 'LR3', 'LR4', 'LR2', '12C', '650S', '570S', '570GT',
        '600LT', '720S', 'Phantom', 'Ghost', 'Wraith', 'Dawn',
        'Continental GT', 'Flying Spur', 'Continental GTC', 'Arnage',
        'Evora', 'Vanquish', 'DB9', 'V8 Vantage', 'V8 Vantage Roadster',
        'Rapide', 'DB11', 'Vantage', 'DBX', 'Bentayga', 'QX30', 'Cullinan',
        'TT Coupe', 'TTS', 'TTS Coupe', 'A-Class', 'CLA',
        'AMG GT 4-Door Coupe', 'SL Roadster', 'AMG GT Coupe', 'GLC-Class',
        'GLC', 'GLB', 'GLA', 'GLA-Class', 'G-Class', 'Metris Cargo Van',
        'SQ5', 'Q8', 'SQ8', 'SQ7', 'Allroad quattro', 'S5 Cabriolet',
        'A5 Cabriolet', 'A8', 'S5', 'A3 Cabriolet', 'S8', 'S4',
        'S5 Sportback', 'A3 Sedan', 'A5 Sportback', 'S3', 'S5 Coupe', 'S6',
        'S7', '2 Series', '4 Series', '1 Series', '6 Series Gran Coupe',
        '6 Series', 'ALPINA B6 Gran Coupe', '6 Series Convertible',
        '6 Series Coupe', '6 Series Gran Turismo', 'X1', 'M2 Coupe',
        'M3 Sedan', 'M4 Coupe', 'M4 Convertible', 'M5', 'M Series', 'X2',
        'X2 M', 'SL-Class', 'SLK', 'SLK-Class', 'CLK-Class', 'CLK',
        'CL-Class', 'CL Class', 'CLA-Class', 'SLR McLaren', 'SLC Roadster',
        'SLS AMG', 'AMG? GT Coupe', 'AMG GT Roadster', 'fortwo', 'Clubman',
        'MINI', 'Cooper', 'Hardtop 2 Door', 'Paceman', 'Convertible',
        'Hardtop 4 Door', 'Cayman', '911', '718', 'Boxster', 'Macan',
        'Cayenne Coupe', 'Cayenne Coupé', 'RS Q8', 'RS 6 Avant', 'R8',
        'TT RS', 'RS 3', 'RS 7', 'RS 5 Coupe', 'RS 5', 'RS4', 'Eos', 'CC',
        'Arteon', 'Golf R', 'Supra', '9-5', 'V60', 'S40', 'C70', 'C30',
        'V50', 'V90', 'V70', 'V70 XC', 'V60 Cross Country', 'XC40',
        'V90 Cross Country', 'Quattroporte', 'Coupe', '4C', 'Giulia',
        'Stelvio', '500L', 'California', '488 Spider', 'FF',
        'California T', '488', '812', '612', '550 Maranello', 'F430',
        '599', '360', 'Gallardo', 'Huracan', 'Levante', 'Urus', 'Insight',
        'C-Max', 'Pacifica Hybrid', 'Fusion Hybrid', 'Fusion Energi',
        'Revero', 'Pathfinder Hybrid', 'Clarity', 'CR-Z', 'Prius Prime',
        'Prius Plug-In', 'Prius c', 'Prius C', 'Prius v', 'HS',
        'ES Hybrid', 'CT', 'UX Hybrid', 'NX Hybrid', 'Ioniq', 'IONIQ',
        'Sonata Hybrid', 'Sonata Plug-in Hybrid', 'Niro'])
            st.selectbox("Drivetrain", index=0, key="drivetrain", options=['4WD', 'FWD', 'RWD'])
            st.number_input("Engine size (L)", value=3.5, key="engine_size", min_value=0.9, step=0.1)
        with col2:
            st.number_input("Year", value=2017, min_value=1886, step=1, key="year")
            st.selectbox("Body type", index=0, key="body_type", options=['coupe', 'sedan', 'pickup', 'suv', 'convertible', 'hatchback',
        'targa', 'passenger_van', 'cargo_van', 'chassis_cab', 'minivan',
        'mini_mpv', 'crossover', 'wagon', 'cutaway', 'micro_car', 'combi',
        'car_van', 'roadster', 'commercial_wagon'])
            st.selectbox("Transmission", index=0, key="transmission", options=['Automatic', 'Manual'])
            st.selectbox("Engine block", index=0, key="engine_block", options=['V', 'I', 'H'])
        with col3:
            st.selectbox("Make", key="make", index=0, options=['acura', 'dodge', 'chrysler', 'ram', 'ford', 'chevrolet', 'buick',
        'cadillac', 'gmc', 'lexus', 'volkswagen', 'bmw', 'mercedes_benz',
        'hummer', 'lincoln', 'volvo', 'infiniti', 'toyota', 'land_rover',
        'audi', 'mini', 'porsche', 'maserati', 'am_general', 'jeep',
        'nissan', 'mazda', 'jaguar', 'honda', 'pontiac', 'oldsmobile',
        'saturn', 'plymouth', 'mercury', 'suzuki', 'kia', 'hyundai',
        'scion', 'mitsubishi', 'subaru', 'fiat', 'genesis', 'lotus',
        'saab', 'ferrari', 'mclaren', 'rolls_royce', 'bentley',
        'aston_martin', 'maybach', 'smart', 'alfa_romeo', 'lamborghini',
        'karma'])
            st.selectbox("Type of vehicle", index=0, key="vehicle_type", options=['Car', 'Truck'])
            st.selectbox("Fuel type", index=0, key="fuel_type", options=['hyrid', 'gasoline', 'other', 'biodiesel'])
            st.selectbox("Province", index=0, key="province", options=['NB', 'QC', 'BC', 'ON', 'AB', 'MB', 'SK', 'NS', 'PE', 'NL', 'YT', 'NC', 'OH','SC'])
        
        st.form_submit_button("Calculate", type="primary")

    # Display the prediction
    # If the value is empty, display a message to click on the button
    # Otherwise, display the prediction
    
    st.write(st.session_state)