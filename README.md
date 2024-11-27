# Tools voor experimentele basistechnieken:

## easyfit.py

### Algemeen

Dit bestand bevat enkel de class EasyFit.
Voor gebruik voldoet de volgende code:

                fit_object = EasyFit(fit_model, "Model naam", xdata, ydata, "$x$ [eenheid]", "$y$ [eenheid]", y_err=yerr, x_err=xerr)

                fit_object.get_general_fit_info(interpretation=True)
                fit_object.plot_model()

y_err en x_err kunnen weggelaten worden, dan gebruiken de functies een fout van 1% op alle datapunten.

Andere manieren om hetzelfde uit te voeren zijn:

                fit_object = EasyFit(fit_model, "Model naam", xdata, ydata, "$x$ [eenheid]", "$y$ [eenheid]", y_err=yerr, x_err=xerr)

                fit_object.get_all_info(interpretation=True)


### Initialisatie

Bij het initialiseren (dus fit_object = Easyfit(...)) moet ervoor gezorgd worden dat de functie fit_model als parameters func(x, *args) heeft. Dit wil zeggen: eerst de variabelen, dan de te fitten parameters.

xdata en ydata zijn best normale python lijsten, en nog geen numpy arrays. Deze worden in de initialisatie omgezet naar numpy arrays.

### Functieoverzicht

De class heeft volgende functies:
- calculate_fit_parameters() -> voert de curve_fit uit voor dit object. Eigenlijk niet zo belangrijk om zelf te gebruiken.
- calculate_statistics() -> berekent statistieken. Net zoals hierboven ook niet enorm belangrijk.
- \__print_method_info_\_() -> Dit is voor intern bedoelt. Boeit dus ook niet echt.
- get_fit_parameters(print_values, combined_info) -> Returned de berekende parameters en hun lijsten in 2 dictionaries. print_values = True zorgt ervoor dat alles ook in de terminal geprint wordt. combined_info is irrelevant en dient enkel voor de interen werking van de functie.
- get_statistic(print_values, combined_info) -> werkt analoog zoals bovenstaand functie
- get_general_fit_info(interpretation) -> BELANGRIJK! Dit is een combinatie van de twee bovenstaande functies. Indien interpretation = True dan geeft hij ook uitleg in de terminal over hoe de statistieken geïnterpreteerd moeten worden. (Absoluut niet van Mathias gestolen). LET OP: Deze functie returned niets!
- get_interpretation_info(combined_info) -> eigenlijk alleen het laatste stukje van bovenstaande functie.
- plot_model() -> plot de datapunten en de fit
- get_all_info(interpretation) -> een combinatie van plot_model() en get_general_fit_info(interpretation).