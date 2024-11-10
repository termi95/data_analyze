INSERT INTO
    laptops (
        Company,
        Product,
        TypeName,
        Inches,
        Ram,
        OS,
        Weight,
        Price_euros,
        Screen,
        ScreenW,
        ScreenH,
        Touchscreen,
        IPSpanel,
        RetinaDisplay,
        CPU_company,
        CPU_freq,
        CPU_model,
        PrimaryStorage,
        SecondaryStorage,
        PrimaryStorageType,
        SecondaryStorageType,
        GPU_company,
        GPU_model
    )
VALUES
    (
        @Company,
        @Product,
        @TypeName,
        @Inches,
        @Ram,
        @OS,
        @Weight,
        @Price_euros,
        @Screen,
        @ScreenW,
        @ScreenH,
        @Touchscreen,
        @IPSpanel,
        @RetinaDisplay,
        @CPU_company,
        @CPU_freq,
        @CPU_model,
        @PrimaryStorage,
        @SecondaryStorage,
        @PrimaryStorageType,
        @SecondaryStorageType,
        @GPU_company,
        @GPU_model
    );