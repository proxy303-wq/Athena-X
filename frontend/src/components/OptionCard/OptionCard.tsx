type Props = {

    pcr: number;

    sentiment: string;

    support: number;

    resistance: number;

    maxPain: number;

};

export default function OptionCard({

    pcr,

    sentiment,

    support,

    resistance,

    maxPain,

}: Props) {

    const item = {

        display: "flex",

        justifyContent: "space-between",

        alignItems: "center",

        marginBottom: 18,

    };

    return (

        <div

            style={{

                background: "#1e293b",

                borderRadius: 18,

                padding: 28,

                boxShadow: "0 0 25px rgba(0,0,0,.25)",

            }}

        >

            <h2
                style={{
                    marginBottom: 24,
                    fontSize: 24,
                }}
            >

                Option Analytics

            </h2>

            <div style={item}>

                <span>PCR</span>

                <strong>{pcr.toFixed(2)}</strong>

            </div>

            <div style={item}>

                <span>Sentiment</span>

                <strong
                    style={{
                        color:
                            sentiment === "BULLISH"
                                ? "#22c55e"
                                : "#ef4444",
                    }}
                >

                    {sentiment}

                </strong>

            </div>

            <div style={item}>

                <span>Support</span>

                <strong>{support}</strong>

            </div>

            <div style={item}>

                <span>Resistance</span>

                <strong>{resistance}</strong>

            </div>

            <div style={item}>

                <span>Max Pain</span>

                <strong>{maxPain}</strong>

            </div>

        </div>

    );

}