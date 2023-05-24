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
    # for match in all_matches:
    #     print(match)


def main():
    # read_pdf("data_pdf.pdf")

    df = pd.DataFrame(read_pdf("data_pdf.pdf"))
    df.to_csv("result_csv_file.csv")


if __name__ == '__main__':
    main()
