{
    "targets": [{
        "target_name": "lws",
        "sources": [ "./src/addon.cpp", "./src/lws.cpp"],
        "cflags_cc!": ["-fno-exceptions"],
        "cflags_cc": ["-std=c++11", "-fexceptions"],
        "conditions": [
                [ 'OS=="mac"', {
                    "xcode_settings": {
                        'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11','-stdlib=libc++','-v'],
                        'OTHER_LDFLAGS': ['-stdlib=libc++'],
                        'MACOSX_DEPLOYMENT_TARGET': '10.7',
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                    }
                }]
        ],
        "link_settings": {
            "libraries": ["-lwebsockets", "-lev"]
        }
    }]
}
