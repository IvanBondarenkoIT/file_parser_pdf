import data_manager as dm
import pandas
import tabula
import re


CSV_FILE_PATH = 'result_csv_file.csv'
NO_VALID_FILE_PATH = "not_valid_data.csv"
PDF_FILE_PATH = 'data_pdf.pdf'


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

    all_matches = re.findall(all_regex, text_content, re.IGNORECASE)

    return all_matches


def main():
    data_interpreter = dm.DataInterpreter()
    data_interpreter.add_data(read_pdf(PDF_FILE_PATH))

    df = pandas.DataFrame(data_interpreter.get_final_values)
    df.to_csv(CSV_FILE_PATH, index=False, header=False)

    df = pandas.DataFrame(data_interpreter.get_not_valid_data)
    df.to_csv(NO_VALID_FILE_PATH, index=False, header=False)


if __name__ == '__main__':
    main()
