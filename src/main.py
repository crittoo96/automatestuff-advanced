import add_logo
import excel_graph
import export_excel_graph
import scraping


def main():
    scraping.run()
    excel_graph.run()
    export_excel_graph.run()
    add_logo.run()


main()
