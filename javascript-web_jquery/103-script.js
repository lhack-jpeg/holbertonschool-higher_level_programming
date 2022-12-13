$(document).ready(() => {
    $("#btn_translate").click(() => {
        const langCode = $("#language_code").val();
        console.log({ langCode });
        $.ajax({
            url: `https://stefanbohacek.com/hellosalut/?lang=${langCode}`,
            type: "get",
            success: (data, status) => {
                $("#hello").text(data.hello);
            },
        });
    });
    $(document).keypress((e) => {
        let keycode = e.keyCode;
        if (keycode == "13") {
            const langCode = $("#language_code").val();
            console.log({ langCode });
            $.ajax({
                url: `https://stefanbohacek.com/hellosalut/?lang=${langCode}`,
                type: "get",
                success: (data, status) => {
                    console.log({ data });
                    $("#hello").text(data.hello);
                },
            });
        }
    });
});
