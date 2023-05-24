import data_manager as dm
import pandas as pd
import tabula
import re


def read_pdf(filename: str):
    pdf_content = tabula.read_pdf(filename, pages="all")
    text_content = "".join(pdf_content[0])

    all_regex = r"(?<=\rname)(.+?)" \
                r"\rdate(.+?)" \
                r"\rnationality(.+?)" \
                r"\raddress(.+?)" \
                r"\rtel(.+?)" \
                r"\remail(.+?)" \
                r"(\rname|Unnamed: 0)"
    all_matches = re.findall(all_regex,
                             text_content, re.IGNORECASE)
    return all_matches


def main():
    # read_pdf("data_pdf.pdf")
    data_interpreter = dm.DataInterpreter()
    data_interpreter.add_data(read_pdf("data_pdf.pdf"))
    df = pd.DataFrame(data_interpreter.get_final_values())
    df.to_csv("result_csv_file.csv", index=False, header=False)


if __name__ == '__main__':
    main()
