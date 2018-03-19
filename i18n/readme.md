These steps are to be followed.

lets say your plugin has name test.py, located in the src folder.

I: 		wrap the "to be translated" strings in "\_()" or "N\_()" function

II: 	`xgettext -i src/test.py -o test.pot -d test_i18n`

III: 	`mkdir -p locale/fr/LC_MESSAGES`

IV:		`msginit -i test.pot -o locale/r/LC_MESSAGES/test_i18n.po -l fr`

#now the .po file would have been generated in the created directory. each string that needs to be translated is `msgid` and the corresponding translated message has to be written in `msgstr` , and change the charset and other data accordingly.

V: 		`cd locale/fr/LC_MESSAGES`

V: 		`msgfmt test_i18n.po -o test_i18n.mo`

VI: 	`cd ../../..`

VII: 	`LANGUAGE=fr python3 test.py`
