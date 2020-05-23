import argparse
import csv
import sys


def process_codigos_postais(filename):
    # cod_distrito,cod_concelho,cod_localidade,nome_localidade,cod_arteria,tipo_arteria,prep1,titulo_arteria,prep2,nome_arteria,local_arteria,troco,porta,cliente,num_cod_postal,ext_cod_postal,desig_postal
    road_types = {}
    road_names = {}
    special = {}
    ignored_header = False

    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if not ignored_header:
                ignored_header = True
                continue

            # get full street name and delete repeated spaces
            name = row[5] + ' ' + row[6] + ' ' + row[7] + ' ' + row[8] + ' ' + row[9]
            name = name.strip()
            name = ' '.join(name.split())

            if name in road_names:
                road_names[name] += 1
            else:
                if len(name) > 0:
                    road_names[name] = 1

            # check for road types
            if len(row[5]) > 0:
                if row[5] in road_types:
                    road_types[row[5]] += 1
                else:
                    road_types[row[5]] = 1

            # special roads or places without road type
            elif len(row[9]) > 0 and row[9] != 'Sem Nome':
                if row[9] in special:
                    special[row[9]] += 1
                else:
                    special[row[9]] = 1

    return road_types, road_names, special


parser = argparse.ArgumentParser(description='Analyse Portuguese road types and names.')
parser.add_argument('file', type=str, help='Source CSV')
parser.add_argument('-t', '--types', help='Print road types', default=False, action='store_true')
parser.add_argument('-n', '--names', help='Print road names', type=int, default=-1, action='store', nargs='?', const=10)
parser.add_argument('-s', '--special', help='Print special places', type=int, default=-1, action='store', nargs='?', const=10)
args = parser.parse_args()

# process DB
road_types, road_names, special = process_codigos_postais(args.file)

print_road_types = args.types
print_road_names = args.names > -1
print_special = args.special > -1

# if not option selected, print road types
if not (print_road_types or print_road_names or print_road_types):
    print_road_types = True

if print_road_types:
    print('{0} unique road types:'.format(len(road_types)))
    for key, value in sorted(road_types.items(), key=lambda item: item[1], reverse=True):
        print('%s: %s' % (key, value))

if print_road_names:
    count = 0
    print('\n{0} Unique road names:'.format(len(road_names)))
    for key, value in sorted(road_names.items(), key=lambda item: item[1], reverse=True):
        print('%s: %s' % (key, value))

        count += 1
        if count > args.names:
            break

if print_special:
    count = 0
    print('\n{0} special places:'.format(len(special)))
    for key, value in sorted(special.items(), key=lambda item: item[1], reverse=True):
        print('%s: %s' % (key, value))

        count += 1
        if count > args.special:
            break
