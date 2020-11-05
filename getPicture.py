import numpy as np
import matplotlib.pyplot as plt
import random as rand
import os

locationDictionary = {'0,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Antimony_380011152_FSTopo.pdf.pdf', '1,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Pollywog_Lake_380011145_FSTopo.pdf.pdf', '2,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Big_Lake_380011137_FSTopo.pdf.pdf', '0,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Grass_Lakes_375211152_FSTopo.pdf.pdf', '1,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Barker_Reservoir_375211145_FSTopo.pdf.pdf', '2,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Posy_Lake_375211137_FSTopo.pdf.pdf', '0,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Sweetwater_Creek_374511152_FSTopo.pdf.pdf', '1,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Griffin_Point_374511145_FSTopo.pdf.pdf', '2,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Wide_Hollow_Reservoir_374511137_FSTopo.pdf.pdf', '3,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Escalante_374511130_FSTopo.pdf.pdf', '1,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Upper_Valley_373711145_FSTopo.pdf.pdf', '2,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Canaan_Creek_373711137_FSTopo.pdf.pdf', '1,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Canaan_Peak_373011145_FSTopo.pdf.pdf', '2,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Death_Ridge_373011137_FSTopo.pdf.pdf', '3,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Jacobs_Reservoir_380011130_FSTopo.pdf.pdf', '4,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Deer_Creek_Lake_380011122_FSTopo.pdf.pdf', '5,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Lower_Bowns_Reservoir_380011115_FSTopo.pdf.pdf', '3,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Roger_Peak_375211130_FSTopo.pdf.pdf', '4,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Boulder_Town_375211122_FSTopo.pdf.pdf', '5,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Steep_Creek_Bench_375211115_FSTopo.pdf.pdf', '6,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Bear_Canyon_380011107_FSTopo.pdf.pdf', '6,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Lamp_Stand_375211107_FSTopo.pdf.pdf', '-1,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Flake_Mountain_East_374511200_FSTopo.pdf.pdf', '-1,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Tropic_Canyon_373711200_FSTopo.pdf.pdf', '0,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37111Pine_Lake_373711152_FSTopo.pdf.pdf', '-3,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Casto_Canyon_374511215_FSTopo.pdf.pdf', '-2,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Flake_Mountain_West_374511207_FSTopo.pdf.pdf', '-3,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Wilson_Peak_373711215_FSTopo.pdf.pdf', '-2,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Bryce_Canyon_373711207_FSTopo.pdf.pdf', '-3,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Tropic_Reservoir_373011215_FSTopo.pdf.pdf', '-2,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Bryce_Point_373011207_FSTopo.pdf.pdf', '-3,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Bull_Rush_Peak_380011215_FSTopo.pdf.pdf', '-2,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Mount_Dutton_380011207_FSTopo.pdf.pdf', '-1,0': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Deep_Creek_380011200_FSTopo.pdf.pdf', '-3,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Blind_Spring_Mountain_375211215_FSTopo.pdf.pdf', '-2,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Adams_Head_375211207_FSTopo.pdf.pdf', '-1,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Cow_Creek_375211200_FSTopo.pdf.pdf', '-5,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Asay_Bench_373011230_FSTopo.pdf.pdf', '-4,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112George_Mountain_373011222_FSTopo.pdf.pdf', '-5,-5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Long_Valley_Junction_372211230_FSTopo.pdf.pdf', '-4,-5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Alton_372211222_FSTopo.pdf.pdf', '-3,-5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Podunk_Creek_372211215_FSTopo.pdf.pdf', '-5,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Fivemile_Ridge_374511230_FSTopo.pdf.pdf', '-4,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Panguitch_374511222_FSTopo.pdf.pdf', '-5,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Haycock_Mountain_373711230_FSTopo.pdf.pdf', '-4,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Hatch_373711222_FSTopo.pdf.pdf', '-7,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Brian_Head_373711245_FSTopo.pdf.pdf', '-6,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Panguitch_Lake_373711237_FSTopo.pdf.pdf', '-7,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Navajo_Lake_373011245_FSTopo.pdf.pdf', '-6,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Henrie_Knolls_373011237_FSTopo.pdf.pdf', '-7,-5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Straight_Canyon_372211245_FSTopo.pdf.pdf', '-6,-5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Strawberry_Point_372211237_FSTopo.pdf.pdf', '-7,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Parowan_374511245_FSTopo.pdf.pdf', '-8,-3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Flanigan_Arch_373711252_FSTopo.pdf.pdf', '-8,-4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Webster_Flat_373011252_FSTopo.pdf.pdf', '-6,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Cottonwood_Mountain_375211237_FSTopo.pdf.pdf', '-5,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Little_Creek_Peak_375211230_FSTopo.pdf.pdf', '-6,-2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Red_Creek_Reservoir_374511237_FSTopo.pdf.pdf', '-4,-1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Panguitch_NW_375211222_FSTopo.pdf.pdf', '-2,-5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/37112Rainbow_Point_372211207_FSTopo.pdf.pdf', '-1,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Malmsten_Peak_381511200_FSTopo.pdf.pdf', '0,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Parker_Knoll_381511152_FSTopo.pdf.pdf', '-1,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Phonolite_Hill_380711200_FSTopo.pdf.pdf', '0,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Angle_380711152_FSTopo.pdf.pdf', '1,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Flossie_Knoll_380711145_FSTopo.pdf.pdf', '0,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Koosharem_383011152_FSTopo.pdf.pdf', '1,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Burrville_383011145_FSTopo.pdf.pdf', '2,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Fish_Lake_383011137_FSTopo.pdf.pdf', '0,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Greenwich_382211152_FSTopo.pdf.pdf', '1,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Abes_Knoll_382211145_FSTopo.pdf.pdf', '2,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Loa_382211137_FSTopo.pdf.pdf', '3,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Lyman_382211130_FSTopo.pdf.pdf', '4,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Flat_Top_382211122_FSTopo.pdf.pdf', '3,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Bicknell_381511130_FSTopo.pdf.pdf', '4,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Torrey_381511122_FSTopo.pdf.pdf', '2,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Smooth_Knoll_380711137_FSTopo.pdf.pdf', '3,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Government_Point_380711130_FSTopo.pdf.pdf', '4,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Blind_Lake_380711122_FSTopo.pdf.pdf', '0,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Sigurd_384511152_FSTopo.pdf.pdf', '1,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Rex_Reservoir_384511145_FSTopo.pdf.pdf', '2,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Gooseberry_Creek_384511137_FSTopo.pdf.pdf', '0,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Water_Creek_Canyon_383711152_FSTopo.pdf.pdf', '1,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Boobe_Hole_Reservoir_383711145_FSTopo.pdf.pdf', '2,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Mount_Terrill_383711137_FSTopo.pdf.pdf', '-1,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39112Scipio_Lake_390011200_FSTopo.pdf.pdf', '-1,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Beehive_Peak_385211200_FSTopo.pdf.pdf', '0,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Aurora_385211152_FSTopo.pdf.pdf', '1,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Salina_385211145_FSTopo.pdf.pdf', '-1,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Richfield_384511200_FSTopo.pdf.pdf', '4,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Geyser_Peak_383011122_FSTopo.pdf.pdf', '5,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Cathedral_Mountain_382211115_FSTopo.pdf.pdf', '5,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Twin_Rocks_381511115_FSTopo.pdf.pdf', '3,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Hilgard_Mountain_383711130_FSTopo.pdf.pdf', '4,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Johns_Peak_383711122_FSTopo.pdf.pdf', '3,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Forsyth_Reservoir_383011130_FSTopo.pdf.pdf', '5,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Grover_380711115_FSTopo.pdf.pdf', '6,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Golden_Throne_380711107_FSTopo.pdf.pdf', '3,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Water_Hollow_Ridge_385211130_FSTopo.pdf.pdf', '4,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Acord_Lakes_385211122_FSTopo.pdf.pdf', '5,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Emery_West_385211115_FSTopo.pdf.pdf', '3,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Yogo_Creek_384511130_FSTopo.pdf.pdf', '4,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Old_Woman_Plateau_384511122_FSTopo.pdf.pdf', '5,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Walker_Flat_384511115_FSTopo.pdf.pdf', '5,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Flagstaff_Peak_390011115_FSTopo.pdf.pdf', '6,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Ferron_390011107_FSTopo.pdf.pdf', '6,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Emery_East_385211107_FSTopo.pdf.pdf', '2,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Mayfield_390011137_FSTopo.pdf.pdf', '3,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Woods_Lake_390011130_FSTopo.pdf.pdf', '2,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38111Steves_Mountain_385211137_FSTopo.pdf.pdf', '-2,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112White_Pine_Peak_384511207_FSTopo.pdf.pdf', '-2,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Elsinore_383711207_FSTopo.pdf.pdf', '-1,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Annabella_383711200_FSTopo.pdf.pdf', '-2,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Antelope_Range_383011207_FSTopo.pdf.pdf', '-1,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Monroe_Peak_383011200_FSTopo.pdf.pdf', '-4,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Shelly_Baldy_Peak_381511222_FSTopo.pdf.pdf', '-3,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Delano_Peak_381511215_FSTopo.pdf.pdf', '-2,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Piute_Reservoir_381511207_FSTopo.pdf.pdf', '-4,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Circleville_Mountain_380711222_FSTopo.pdf.pdf', '-3,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Circleville_380711215_FSTopo.pdf.pdf', '-2,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Junction_380711207_FSTopo.pdf.pdf', '-5,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Pole_Mountain_382211230_FSTopo.pdf.pdf', '-4,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Mount_Belknap_382211222_FSTopo.pdf.pdf', '-5,2': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Black_Ridge_381511230_FSTopo.pdf.pdf', '-5,1': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Kane_Canyon_380711230_FSTopo.pdf.pdf', '-5,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Dog_Valley_Peak_383711230_FSTopo.pdf.pdf', '-4,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Red_Ridge_383711222_FSTopo.pdf.pdf', '-5,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Cove_Fort_383011230_FSTopo.pdf.pdf', '-4,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Trail_Mountain_383011222_FSTopo.pdf.pdf', '-4,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Kanosh_384511222_FSTopo.pdf.pdf', '-3,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Sunset_Peak_384511215_FSTopo.pdf.pdf', '-3,5': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Joseph_Peak_383711215_FSTopo.pdf.pdf', '-3,4': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Marysvale_Canyon_383011215_FSTopo.pdf.pdf', '-3,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39112Holden_390011215_FSTopo.pdf.pdf', '-2,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39112Coffee_Peak_390011207_FSTopo.pdf.pdf', '-3,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Fillmore_385211215_FSTopo.pdf.pdf', '-2,7': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Mount_Catherine_385211207_FSTopo.pdf.pdf', '-3,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Mount_Brigham_382211215_FSTopo.pdf.pdf', '-2,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Marysvale_382211207_FSTopo.pdf.pdf', '-1,3': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Marysvale_Peak_382211200_FSTopo.pdf.pdf', '-5,6': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/38112Sixmile_Point_384511230_FSTopo.pdf.pdf', '3,10': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Ephraim_391511130_FSTopo.pdf.pdf', '4,10': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Danish_Knoll_391511122_FSTopo.pdf.pdf', '2,9': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Sterling_390711137_FSTopo.pdf.pdf', '3,9': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Black_Mountain_390711130_FSTopo.pdf.pdf', '4,9': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Ferron_Reservoir_390711122_FSTopo.pdf.pdf', '4,8': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Heliotrope_Mountain_390011122_FSTopo.pdf.pdf', '2,12': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Fountain_Green_South_393011137_FSTopo.pdf.pdf', '2,11': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Wales_392211137_FSTopo.pdf.pdf', '3,11': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Chester_392211130_FSTopo.pdf.pdf', '4,11': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Spring_City_392211122_FSTopo.pdf.pdf', '1,12': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Levan_393011145_FSTopo.pdf.pdf', '0,11': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Skinner_Peaks_392211152_FSTopo.pdf.pdf', '1,11': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Chriss_Canyon_392211145_FSTopo.pdf.pdf', '5,10': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Joes_Valley_Reservoir_391511115_FSTopo.pdf.pdf', '6,10': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Mahogany_Point_391511107_FSTopo.pdf.pdf', '5,9': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Ferron_Canyon_390711115_FSTopo.pdf.pdf', '6,9': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111The_Cap_390711107_FSTopo.pdf.pdf', '1,14': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Mona_394511145_FSTopo.pdf.pdf', '2,14': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Nebo_Basin_394511137_FSTopo.pdf.pdf', '3,14': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Spencer_Canyon_394511130_FSTopo.pdf.pdf', '1,13': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Nephi_393711145_FSTopo.pdf.pdf', '2,13': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Fountain_Green_North_393711137_FSTopo.pdf.pdf', '2,16': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/40111Spanish_Fork_400011137_FSTopo.pdf.pdf', '3,16': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/40111Spanish_Fork_Peak_400011130_FSTopo.pdf.pdf', '4,16': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/40111Billies_Mountain_400011122_FSTopo.pdf.pdf', '2,15': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Payson_Lakes_395211137_FSTopo.pdf.pdf', '3,15': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Birdseye_395211130_FSTopo.pdf.pdf', '4,15': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Thistle_395211122_FSTopo.pdf.pdf', '4,14': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Indianola_394511122_FSTopo.pdf.pdf', '5,15': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Mill_Fork_395211115_FSTopo.pdf.pdf', '6,15': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Tucker_395211107_FSTopo.pdf.pdf', '6,14': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Scofield_Reservoir_394511107_FSTopo.pdf.pdf', '4,13': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Fairview_393711122_FSTopo.pdf.pdf', '5,13': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Fairview_Lakes_393711115_FSTopo.pdf.pdf', '6,13': '/home/m/PycharmProjects/mapsProject/allPdfs/UTAH/39111Scofield_393711107_FSTopo.pdf.pdf'}
for key in locationDictionary:
    split = str(key).split(',')
    x = int(split[0])
    y = int(split[1])
    plt.scatter(x, y, color='gray')

plt.savefig("mychart.png")