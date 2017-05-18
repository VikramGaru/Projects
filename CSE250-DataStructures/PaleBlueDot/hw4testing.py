import datetime
import webbrowser

import PaleBlueDot

# A function just for fun and to help with debugging. This is not required for the assignment
def openMap(location):
    url = "http://maps.google.com/maps?t=m&q=loc:" + \
          str(location.getLatitude()) + "+" + str(location.getLongitude())
    webbrowser.open_new(url)

def floatCompare(float1, float2):
    epsilon = 0.001
    percentEpsilon = 0.01
    if abs(float1 - float2) < epsilon:
        return True
    if abs(float1 - float2) / float1 < percentEpsilon:
        return True
    if abs(float1 - float2) / float2 < percentEpsilon:
        return True
    return False


def testPart1():
    pbd = PaleBlueDot.PaleBlueDot("data/worldCities-abridged.csv")
    cityCases = [['nakhashi qalandari', '08', 'af', '33.149644', '67.581833'],
                 ['navarsup', '27', 'af', '34.417222', '67.839722'],
                 ['jaronisht', '43', 'al', '40.9586111', '20.2602778'],
                 ['weissenstein', '02', 'at', '46.6', '14.866667'], ['sirvan', '07', 'az', '39.937877', '48.928554'],
                 ['rose hill', '09', 'bb', '13.2666667', '-59.6166667'], ['denguilga', '15', 'bf', '13.4', '-1.7'],
                 ['goussin sare', '03', 'bj', '10.9166667', '3.7333333'],
                 ['bao bato', '04', 'cf', '4.3666667', '16.0833333'], ['gongchi', '14', 'cn', '28.901', '87.701'],
                 ['paimala', '15', 'fi', '60.516667', '22.35'], ['lungur', '08', 'id', '-7.7394', '111.7933'],
                 ['saradan', '30', 'id', '-6.443056', '108.077222'],
                 ['istgah-e garmsar', '25', 'ir', '35.234549', '52.309415'],
                 ['maktokpo', '17', 'kp', '41.1002778', '129.1708333'],
                 ['menawa', '29', 'lk', '7.1833333', '80.4666667'],
                 ['rancho pesqueira', '26', 'mx', '30.85', '-112.983333'],
                 ['guraka', '46', 'ng', '10.672752', '8.866122'],
                 ['stokt', '05', 'nl', '51.480522', '6.151746'],
                 ['singeru de padure', '27', 'ro', '46.633333', '24.666667'],
                 ['vestansjo', '23', 'se', '65.733333', '15.066667'], ['sarica', '52', 'tr', '40.435005', '37.779325'],
                 ['tapingshan', '04', 'tw', '24.5', '121.4833333'],
                 ['simba chinzachi', '03', 'tz', '-5.9666667', '35.5666667'],
                 ['zelen', '19', 'ua', '51.69188', '26.206009'], ['olanta', 'pa', 'us', '40.9166667', '-78.5066667'],
                 ['garretts mill', 'tn', 'us', '36.4263889', '-85.2983333'],
                 ['muyapa', '14', 've', '9.1244444', '-71.1222222']]

    print("testing getCityLocation")
    for case in cityCases:
        city = case[0]
        region = case[1]
        country = case[2]
        lat = float(case[3])
        long = float(case[4])
        answer = pbd.getCityLocation(city, region, country)
        if answer is None or not floatCompare(answer.getLatitude(), lat) or \
                not floatCompare(answer.getLongitude(), long):
            print("incorrect on: " + str(case))
            print("returned: " + str(answer))
            return

    observatoryCases = [['038', 'Trieste', 45.45088291312654, 13.7704], ['191', 'Dushanbe', 38.37366947869566, 68.7811],
                        ['280', 'Lilienthal', 52.95577845657219, 8.9118], ['469', 'Courroux', 47.16444631822856, 7.382],
                        ['587', 'Sormano', 45.69156872030071, 9.23025],
                        ['827', 'Saint-Felicien', 48.46037167553807, 287.5393],
                        ['932', 'John J. McCarthy Obs., New Milford', 41.3347908554966, 286.57394],
                        ['A10', 'Observatorio Astronomico de Corbera', 41.075707375617725, 1.9281],
                        ['B87', 'Banyoles', 41.92302381417147, 2.7701], ['C23', 'Olmen', 50.95229218749451, 5.15439],
                        ['E89', 'Geyserland Observatory, Pukehangi', -37.94924617039921, 176.204],
                        ['H20', 'Eastern Illinois University Obs., Charleston', 39.28849054899743, 271.81682],
                        ['J64', 'La Mata', 37.84187622433411, 359.3459],
                        ['Q21', 'Southern Utsunomiya', 36.32351076123217, 139.85335],
                        ['W81', 'Nebula Knoll Observatoy, East Wakefield', 43.473737424064474, 288.99967]]

    print("testing getObservatoryName")
    for case in observatoryCases:
        code = case[0]
        name = case[1]
        # lat = float(case[2])
        # long = float(case[3])
        answer = pbd.getObservatoryName(code)
        if answer != name:
            print("incorrect on: " + str(case))
            print("returned: " + str(answer))
            return

    print("passed part 1")


def testPart2():
    pbd = PaleBlueDot.PaleBlueDot("data/worldCities-abridged.csv")

    observatoryCases = [['038', 'Trieste', 45.45088291312654, 13.7704], ['191', 'Dushanbe', 38.37366947869566, 68.7811],
                        ['280', 'Lilienthal', 52.95577845657219, 8.9118], ['469', 'Courroux', 47.16444631822856, 7.382],
                        ['587', 'Sormano', 45.69156872030071, 9.23025],
                        ['827', 'Saint-Felicien', 48.46037167553807, 287.5393],
                        ['932', 'John J. McCarthy Obs., New Milford', 41.3347908554966, 286.57394],
                        ['A10', 'Observatorio Astronomico de Corbera', 41.075707375617725, 1.9281],
                        ['B87', 'Banyoles', 41.92302381417147, 2.7701], ['C23', 'Olmen', 50.95229218749451, 5.15439],
                        ['E89', 'Geyserland Observatory, Pukehangi', -37.94924617039921, 176.204],
                        ['H20', 'Eastern Illinois University Obs., Charleston', 39.28849054899743, 271.81682],
                        ['J64', 'La Mata', 37.84187622433411, 359.3459],
                        ['Q21', 'Southern Utsunomiya', 36.32351076123217, 139.85335],
                        ['W81', 'Nebula Knoll Observatoy, East Wakefield', 43.473737424064474, 288.99967]]

    print("testing getObservatoryLocation")
    for case in observatoryCases:
        code = case[0]
        # name = case[1]
        lat = float(case[2])
        long = float(case[3])
        answer = pbd.getObservatoryLocation(code)
        if answer is None or not floatCompare(answer.getLatitude(), lat) or not floatCompare(answer.getLongitude(),
                                                                                             long):
            print("incorrect on: " + str(case))
            print("returned: " + str(answer))
            return

    circleCases = [
        [-65.82622902173087, -10.413995903142677, -57.06605394309698, -1.6852507608132896, 1076.6073820337647],
        [45.211842149799, -130.4891518150788, 47.069863176469966, 50.09396969714385, 9753.670896289728],
        [12.733424251291297, -156.4760478450378, -84.91802614609509, -26.574791183883207, 11782.25965654898],
        [-47.505668886687864, 65.67286957925029, -12.303554187002717, -132.77988602992914, 13117.215339890268],
        [50.65130296473876, -0.09760419125686326, 35.59055263126652, 127.60084945744336, 9146.355233414442],
        [-52.959846226337206, -176.43565915418046, 2.401189601495844, -82.4930163292415, 10484.692146465002],
        [51.96699774944193, 57.79872594085987, -26.640423085039984, 145.1209905287942, 12132.923524007732],
        [19.516321910709024, 40.45207424068866, 20.360549974848425, -9.691523969140462, 5221.444756456884],
        [-62.33726674816904, -59.41385173223716, -59.68123573658113, 15.435629636511123, 3817.2171995962453],
        [16.916846298021824, 99.36010005590339, 32.273834058281935, 134.3735365603622, 3905.771096600865],
        [44.00379487807663, -5.109581397033821, 70.96384635900728, -13.309948602704338, 3031.3568024347423],
        [26.29085337241824, 52.055783920621224, -47.62943741693517, -113.84497683318851, 17341.701627808172],
        [1.5134631155656137, 91.99545100357818, 1.4727320285462895, -142.07437596423213, 13994.324264520517],
        [65.99726282871544, 178.2413480973383, -65.33142549354278, -0.5208438224991596, 19921.824514663906],
        [34.40896510089381, 50.613693992888074, -1.5756224176193143, 63.16178611714204, 4210.221622959795],
        [-57.27280246818704, 3.6500229538738154, 67.89702972075551, 60.47573131725014, 14669.04228027984],
        [38.73983094426407, -101.71443996270631, -39.66339710012329, 87.73725638698272, 19194.597423707077],
        [-4.5406128946344495, 132.70241407445752, 36.84166465656841, -147.77736065562297, 9384.48996714607],
        [82.29431655680753, 149.5380038951754, 50.31308885445304, -56.84059386080908, 5192.205624717878],
        [4.1518070198314945, 51.73440897607125, 77.31721371780156, -89.3360593681323, 10643.876251120455]]

    print("testing greatCircleDistance")
    for case in circleCases:
        location1 = PaleBlueDot.Location(float(case[0]), float(case[1]))
        location2 = PaleBlueDot.Location(float(case[2]), float(case[3]))
        distance = float(case[4])
        answer = pbd.greatCircleDistance(location1, location2)
        if answer is None or not floatCompare(answer, distance):
            print("incorrect on: " + str(case))
            print("returned: " + str(answer))
            #return

    print("passed part 2")


def testPart3():
    pbd = PaleBlueDot.PaleBlueDot("data/worldCities-abridged.csv")

    locationCases = [[-59.116750451263044, -132.05264419820617, '484'],
                     # [80.75337513314113, 58.26933192208105, '244'],
                     [-31.949879152814958, -68.59964202172532, '829'],
                     # [6.8028962278636556, -15.427292518753802, 'J55'],
                     [-89.29777606568094, 157.51420744774668, '474'],
                     [-82.07951454877195, 158.57314381031205, '474'],
                     [6.067438879817985, 157.19955477525747, 'E04'],
                     [-62.792118513039455, 24.47077506079603, '641'],
                     [-60.06043006324434, -93.75667489852125, 'I47'],
                     [33.07758819672689, 76.36132849445238, 'N55'],
                     [42.253855085649406, -22.052386682674893, 'J11'],
                     [18.717166604271597, 126.15047530819845, 'D44'],
                     [-45.04650887401361, -74.03937130286809, 'I47'],
                     # [82.19394416562471, -23.936108962758027, '244'],
                     [-79.17183049060293, 118.47180282128852, '474'],
                     [-19.55474114220273, -96.3868269012692, '800'],
                     [20.22640655492431, 140.39128820430864, 'E04'],
                     [35.24115311484863, -140.4104508171156, 'U54'],
                     [-44.472297726188664, 138.76620974532267, 'E03'],
                     [-62.031559089131676, -0.21339714853300507, '641']]

    print("testing getClosestObservatory")
    for case in locationCases:
        location = PaleBlueDot.Location(float(case[0]), float(case[1]))
        observatory = case[2]
        answer = pbd.getClosestObservatory(location)
        if answer != observatory:
            print("incorrect on: " + str(case))
            print("returned: " + str(answer))
            return

    # getClosestObservatoryToISS and nextPassTime rely on real time data. Please verify based on the current location
    # of the ISS: http://iss.astroviewer.net/

    print("passed part 3 (pending ISS functions)")


def testPart4():
    pbd = PaleBlueDot.PaleBlueDot("data/worldCities-abridged.csv")

    # locationCases = [
    #     [89.78777201874524, 117.78888743855134, ['craig harbour', '14', 'ca']],
    #     [-63.45755859772201, -58.410776476409936, ['mision fagnano', '23', 'ar']],
    #     [53.44187333740385, -156.5855303213775, ['nuchek', 'ak', 'us']],
    #     [78.28445799300192, -164.19912449015223, ['kolyuchino', '15', 'ru']],
    #     [-85.66237247149199, -0.0778051918210565, ['grytviken', '00', 'gs']],
    #     [-40.208065215071585, -172.898517614653, ['puketapu', 'f9', 'nz']],
    #     [52.060428722971636, -102.6080600172687, ['kelso station', '11', 'ca']],
    #     [34.79479955299793, 40.48432796107454, ['aauoaj el falaj', '07', 'sy']],
    #     [64.48013019751892, 122.07109278763062, ['vilyuysk', '63', 'ru']],
    #     [-51.42192229522117, -92.80228260605193, ['tamel aiken', '20', 'ar']],
    #     [49.319736396847134, 72.73271940677026, ['karagocha pervaya', '12', 'kz']],
    #     [-40.273298061866434, -101.86389415309746, ['puntra', '14', 'cl']],
    #     [4.233478966049361, -63.15788174386964, ['caruana de montana', '06', 've']],
    #     [48.2578149844845, 117.73550010047461, ['khaketay', '06', 'mn']],
    #     [-3.0098072733544257, -110.21244269688975, ['el ayacaixtle', '12', 'mx']],
    #     [78.39889646638315, -58.63787084135808, ['qeqertaq', '01', 'gl']],
    #     [-81.12189427859448, -59.518107469883574, ['mision fagnano', '23', 'ar']],
    #     [77.2057515676376, -142.506647976742, ['fink creek', 'ak', 'us']],
    #     [-17.13545539114284, -138.32611597015978, ['faaone', '00', 'pf']],
    #     [-67.80531026121122, -173.9873379989031, ['kaka point', 'f7', 'nz']]]

    locationCases = [[18.03435984350891, -30.262993216040513, ['seladinha', '00', 'cv']],
                     [2.335499103702915, -136.06039911062805, ['faaone', '00', 'pf']],
                     [-50.48190997649673, -160.96691317373762, ['puketapu', 'f9', 'nz']],
                     [13.374972602361098, 93.84400375934098, ['austinabad', '01', 'in']],
                     [-48.52178392020969, -83.15927336986893, ['tamel aiken', '20', 'ar']],
                     [87.29718461385468, -149.67139271553384, ['craig harbour', '14', 'ca']],
                     [-76.68774776560633, -9.238586517045292, ['grytviken', '00', 'gs']],
                     [76.01147551118854, 68.79559773739047, ['novoluzino', '74', 'ru']],
                     [47.37496994864222, 92.7613454306636, ['altan teeli', '12', 'mn']],
                     [48.1714161496497, 28.237062052296068, ['sobari', '87', 'md']],
                     [-31.93485361800819, 35.681330453367224, ['egolokodo', '02', 'za']],
                     [-18.97528087022353, 162.0691154157704, ['karembe', '00', 'nc']],
                     [-29.078432107055285, 21.753435928799007, ['de bruynsrus', '08', 'za']],
                     [-69.97054234480139, 165.61836767162958, ['kaka point', 'f7', 'nz']],
                     [19.78515801566087, -83.2827582849716, ['the common', '00', 'ky']],
                     [58.99000360709621, -72.30582724236271, ['landrienne', '10', 'ca']],
                     [51.764776776593806, -132.34931105824188, ['bellakula', '02', 'ca']],
                     [-70.91916872810617, -135.65225032055315, ['mision fagnano', '23', 'ar']],
                     [7.645209675550703, 177.0130937888182, ['tebatibaki', '00', 'ki']],
                     [-32.98761471491269, -156.0270750287023, ['area', '00', 'pf']],
                     [36.81108802305248, 124.49861136944116, ['tongnaegol', '06', 'kp']],
                     [-67.63894270803758, 35.36876496707194, ['marina glades', '05', 'za']],
                     [85.84679190697074, 147.27126959772016, ['nagym', '63', 'ru']],
                     [78.49744265826064, 148.13092507920555, ['salgyaki', '63', 'ru']],
                     [73.07081351318593, -71.17452195578828, ['qeqertaq', '01', 'gl']],
                     [41.842850576140705, 37.503304605543036, ['kurma', '52', 'tr']],
                     [-19.458428764559713, -179.22240326736556, ['avea', '03', 'fj']],
                     [-36.22750290888809, -99.51422601659793, ['puntra', '14', 'cl']],
                     [85.14464724978805, -8.370180922033512, ['qeqertaq', '01', 'gl']],
                     [-66.57136056577764, 58.25411377997506, ['richmond', '05', 'za']],
                     [-37.89243027524403, -52.57770656620538, ['barrancas', '14', 'uy']],
                     [6.252704193389604, 68.71341324663933, ['narakal', '13', 'in']],
                     [-57.61303757733434, 114.26968733390106, ['forest grove', '08', 'au']],
                     [80.08680706627436, -131.4366447271582, ['craig harbour', '14', 'ca']],
                     [3.164988742368962, 8.82501098491636, ['basakato', '05', 'gq']],
                     [16.92602812650975, 112.08829325775281, ['wangcun', '31', 'cn']],
                     [-8.70307931120766, -90.08512075042246, ['la luz hacienda', '20', 'pe']],
                     [-0.3856836836053503, 132.58737273231418, ['warbo', '39', 'id']],
                     [-36.89977320906904, 13.067221806963516, ['wildschutsbrand', '11', 'za']],
                     [50.417659882421276, -8.304382814831882, ['pallas', '04', 'ie']],
                     [-12.712129023963413, 49.37421522472968, ['analamisondrotra', '01', 'mg']],
                     [60.77671219990148, 136.97315572062428, ['verkhnyaya mar', '63', 'ru']],
                     [4.822671672185862, 141.31319090099294, ['thabeth', '04', 'fm']],
                     [-9.816710055996381, 142.78132960090744, ['jibara', '06', 'pg']],
                     [58.62156986468432, -141.0399257345035, ['nuchek', 'ak', 'us']],
                     [-10.87814881567084, 91.78051300830884, ['sabulubbek', '24', 'id']],
                     [80.91519058648154, 121.57098538444524, ['nagym', '63', 'ru']],
                     [-78.94245135845262, 70.03420424877103, ['grytviken', '00', 'gs']],
                     [-70.41400745753042, 164.54888591090213, ['kaka point', 'f7', 'nz']],
                     [-14.74179912560686, -49.5842655528603, ['rubiataba', '29', 'br']]]

    print("testing getClosestCity")
    for case in locationCases:
        location = PaleBlueDot.Location(float(case[0]), float(case[1]))
        city = case[2]
        answer = pbd.getClosestCity(location)
        if answer is None or len(answer) != 3 or answer[0] != city[0] or answer[1] != city[1] or answer[2] != city[2]:
            print("incorrect on: " + str(case))
            print("returned: " + str(answer))
            #return

    print("loading 2.24 million cities..")
    pbd = PaleBlueDot.PaleBlueDot("data/worldCities.csv")

    # locationCases = [[-60.61384878636903, 112.80061386895574, ['pelverata', '06', 'au']],
    #                  [74.22080553757021, 41.37047409880728, ['pankova', '06', 'ru']],
    #                  [32.9576123592076, -9.706268999217258, ['dar cheikh ahmed ou ali', '51', 'ma']],
    #                  [86.28591224853758, 162.67948539099427, ['alert', '14', 'ca']]]

    locationCases = [[25.227576343747003, -104.54040854574944, ['pelillos', '10', 'mx']],
                     [-60.61384878636903, 112.80061386895574, ['pelverata', '06', 'au']],
                     [74.22080553757021, 41.37047409880728, ['pankova', '06', 'ru']],
                     [32.9576123592076, -9.706268999217258, ['dar cheikh ahmed ou ali', '51', 'ma']],
                     [86.28591224853758, 162.67948539099427, ['alert', '14', 'ca']],
                     [-58.813353080798, 134.492742411723, ['pelverata', '06', 'au']],
                     [2.393198091481324, -154.5201148506609, ['london', '00', 'ki']],
                     [-84.4334934350209, -46.19237586538432, ['puerto espanol', '23', 'ar']],
                     [-31.88083586364462, 51.77443384572169, ['faradofay', '06', 'mg']],
                     [-45.104057618694036, 59.54240641510495, ['port-aux-francais', '00', 'tf']],
                     [39.82083542751499, 141.37766174567872, ['modegi', '16', 'jp']],
                     [85.81160435120469, -13.157132929022566, ['nord', '01', 'gl']],
                     [-51.35695563621761, 72.5495101560937, ['port-aux-francais', '00', 'tf']],
                     [50.692775665569144, -43.651931190262786, ['elliston', '05', 'ca']],
                     [64.24441120057077, -88.67478681308171, ['chesterfield', '14', 'ca']],
                     [-4.316671739080604, -160.7322719432621, ['omoka', '00', 'ck']],
                     [75.8438166543967, 5.1947014243892795, ['barentsburg', '00', 'sj']],
                     [-1.7411376444167246, -111.87574845543925, ['santo tomas', '01', 'ec']],
                     [56.47669573152564, 80.5399445909614, ['pikuleva', '75', 'ru']],
                     [63.715308306372265, -157.83172734624245, ['kaltag', 'ak', 'us']],
                     [-89.64069808998224, -114.65694996244028, ['puerto navarino', '10', 'cl']],
                     [2.766519260250874, 61.369738991907184, ['la reunion', '08', 'sc']],
                     [-72.64477045741533, 142.43438215170136, ['pelverata', '06', 'au']],
                     [62.60197174988494, 81.93173121020737, ['van-emtorskiye', '32', 'ru']],
                     [47.03032752414873, -166.17141624497407, ['nikolski', 'ak', 'us']],
                     [-59.6477543712692, 113.11489861605293, ['pelverata', '06', 'au']],
                     [-18.42665701948603, -96.74937014800102, ['hanga roa', '01', 'cl']],
                     [-81.4854989701825, -8.439346205573742, ['grytviken', '00', 'gs']],
                     [86.91125196561688, 162.10405672872344, ['alert', '14', 'ca']],
                     [3.7586486648385886, -6.6968190678825295, ['dodo', '76', 'ci']],
                     [-16.45078854942247, -81.5414384827452, ['laguna grande', '11', 'pe']],
                     [-3.707280999142, -138.92597452923465, ['anaho', '00', 'pf']],
                     [21.0925096285292, -103.26372368320696, ['animas', '32', 'mx']],
                     [-81.29253312263637, 179.16459924768628, ['half-moon bay', 'g2', 'nz']],
                     [-81.941612219771, 55.02273037470306, ['port-aux-francais', '00', 'tf']],
                     [-49.01818540310519, -53.389618224567656, ['johnson harbour settlement', '00', 'fk']],
                     [-4.884817716621299, 101.75284978730616, ['barbau', '03', 'id']],
                     [-61.54252921764874, -63.25867548718318, ['puerto espanol', '23', 'ar']],
                     [19.099981924339076, -19.51410691217211, ['el mamghar', '08', 'mr']],
                     [-49.31731801115913, -99.58470717043144, ['estancia pudeto', '10', 'cl']],
                     [84.79158061437542, -22.477125524283167, ['nord', '01', 'gl']],
                     [28.42516483376376, 14.401771611430036, ['dabdab', '13', 'ly']],
                     [77.21869846361903, 176.67894583929012, ['perkatkun', '15', 'ru']],
                     [76.0710541524532, -171.46719866227693, ['perkatkun', '15', 'ru']],
                     [53.16204724648486, -141.48857777452608, ['port armstrong', 'ak', 'us']],
                     [0.5980673293067866, 16.88842207858417, ['ekondjo', '10', 'cg']],
                     [51.53574092619482, -154.71001802704757, ['unga', 'ak', 'us']],
                     [0.31681721614656055, 17.958097643422406, ['loka', '02', 'cd']],
                     [-75.48702537620055, 74.25116559211793, ['port-aux-francais', '00', 'tf']],
                     [10.03984340966636, 69.64553532458649, ['kavaratti', '14', 'in']]]

    print("start part 4 timing")
    startTime = datetime.datetime.now()

    for case in locationCases:
        location = PaleBlueDot.Location(float(case[0]), float(case[1]))
        city = case[2]
        answer = pbd.getClosestCity(location)
        if answer is None or len(answer) != 3 or answer[0] != city[0] or answer[1] != city[1] or answer[2] != city[2]:
            print("incorrect on: " + str(case))
            print("returned: " + str(answer))
            return

    endTime = datetime.datetime.now()

    print("part 4 runtime: " + str(endTime - startTime))

    # getClosestCityToISS relies on real time data.


testPart1()
testPart2()
testPart3()
testPart4()