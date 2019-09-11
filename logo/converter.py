"""A helper module to convert the earthquake XML file to a CSV file."""

from typing import Dict, List

from xml.dom import minidom

import csv
import pathlib


def xml_to_csv(xml_file: pathlib.Path) -> List[Dict]:
    """Convert a XML file to a CSV file."""
    earthquakedata = minidom.parse(str(xml_file))

    earthquakeinfo = earthquakedata.getElementsByTagName("earthquakeinfo")

    output: List[Dict] = []

    for info in earthquakeinfo:

        quality = info.getElementsByTagName("quality")[0].firstChild.data

        magnitude = float(
            info.getElementsByTagName("magnitudeValue")[0].firstChild.data)

        if quality == "A" or quality == "B":

            if magnitude > 4:
                item = {}
                item["depth"] = \
                    info.getElementsByTagName("depth")[0].firstChild.data

                if magnitude > 7:
                    magnitude = magnitude * 2.0
                elif magnitude > 6:
                    magnitude = magnitude * 1.5
                elif magnitude > 5:
                    magnitude = magnitude * 1.2

                item["magnitude"] = magnitude
                item["longitude"] = info.getElementsByTagName(
                    "epicenterLon")[0].firstChild.data
                item["latitude"] = info.getElementsByTagName(
                    "epicenterLat")[0].firstChild.data

                output.append(item)

    return output

if __name__ == "__main__":
    data_file = pathlib.Path("CWB-EQ-Catalog-1999.xml")

    with open("earthquake.csv", "w", newline="") as csvfile:
        fieldnames = ["longitude", "latitude", "magnitude", "depth"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for item in xml_to_csv(xml_file=data_file):
            writer.writerow(item)
